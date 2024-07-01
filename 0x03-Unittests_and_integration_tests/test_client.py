#!/usr/bin/env python3

"""Test module for client.py"""

from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    '''
    This class is for testing GithubOrgClient
    '''
    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        '''
        This method is for testing org
        '''
        gh_org_clt = GithubOrgClient(org_name)
        self.assertEqual(gh_org_clt.org, {"payload": True})
        theurl = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(theurl)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org) -> None:
        '''
        This method is for testing public_repos_url
        '''
        load = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = load
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client._public_repos_url,
                         load["repos_url"])

    @patch("client.get_json",
           return_value=[{"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json) -> None:
        '''
        This method is for testing public_repos
        '''
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            gth_org_clt = GithubOrgClient("google")
            self.assertEqual(gth_org_clt.public_repos(),
                             ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected_result) -> None:
        '''
        This method is for testing has_license
        '''
        gh_org_clt = GithubOrgClient("google")
        self.assertEqual(
            gh_org_clt.has_license(repo, license_key), expected_result
        )


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''
    This class is for testing GithubOrgClient
    '''
    @classmethod
    def setUpClass(cls):
        '''
        This method is for testing setUpClass
        '''
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            '''
            This method is for testing side_effect
            '''
            class MockResponse:
                def __init__(self, json_data):
                    self.json_data = json_data

                def json(self):
                    return self.json_data

            if url.endswith("/orgs/google"):
                return MockResponse(cls.org_payload)
            elif url.endswith("/orgs/google/repos"):
                return MockResponse(cls.repos_payload)
            else:
                return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        '''
        This method is for testing tearDownClass
        '''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''
        This method is for testing public_repos
        '''
        gh_org_clt = GithubOrgClient("google")
        self.assertEqual(gh_org_clt.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        '''
        This method is for testing public_repos_with_license
        '''
        gh_org_lient = GithubOrgClient("google")
        self.assertEqual(gh_org_lient.public_repos(license="apache-2.0"),
                         self.apache2_repos)
