# GitHub App setup shortcuts

These links are convenience entry points for the human setup flow documented in [`GITHUB_APP_SETUP.md`](GITHUB_APP_SETUP.md).

## OpenSiro owner shortcuts

- [Create the OpenSiro Executor Provenance App with pre-filled settings](https://github.com/organizations/opensiro/settings/apps/new?name=OpenSiro%20Executor%20Provenance&description=Dedicated%20executor%20identity%20for%20bounded%20OpenSiro%20VSM%20provenance%20trials.&url=https%3A%2F%2Fgithub.com%2Fopensiro%2Fvsm-oss-organization&public=false&webhook_active=false&contents=write&issues=write&pull_requests=write)
- [Manage OpenSiro GitHub Apps](https://github.com/organizations/opensiro/settings/apps)
- [Manage OpenSiro GitHub App installations](https://github.com/organizations/opensiro/settings/installations)

The pre-filled creator link sets the suggested App name, description, homepage, private visibility, disabled webhook delivery, and the initial repository permissions (`contents`, `issues`, `pull_requests` = write). GitHub still shows the form before creation, so the owner should review the configuration before submitting it.

## GitHub references

- [Register a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)
- [Registration URL parameters](https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-using-url-parameters)
- [Manage private keys](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps)
- [Generate an installation access token](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)
- [GitHub App security best practices](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app)

These shortcuts do not change the security boundary in the main guide. App identifiers and configuration are public evidence; private keys, App JWTs, and installation tokens remain secrets.
