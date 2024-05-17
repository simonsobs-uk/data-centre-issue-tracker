# Making a new release

## Building

For the documentation, we aim to deliver it in these formats: HTML, ePub, PDF.

Per commit in `main` branch, if it builds successfully, it will deploy to the `latest` version in Read the Doc: <https://docs.souk.ac.uk/en/latest/>, and also in GitHub Pages: <https://docs-ci.souk.ac.uk/>.

To build the project, `makefile` is used. `make doc` (after you activated the `soukdc` conda environment) should builds the HTML documentation.

:::{warning}
To ensure the documentation deploys to Read the Doc successfully, make sure there is no warnings when making the documentation. To ensure the cache isn't hiding some errors, you may run

```sh
make clean && make all
```
:::

All targets (HTML, ePub, PDF) is deployed to Read the Doc automatically.

## Serving

When authoring the documentation, you may want to have the HTML built at real time. Use

```sh
# after activating your conda environment soukdc
make serve
```

## Semantic versioning and `bump-my-version`

[Semantic versioning](https://semver.org) is followed, with the `MAJOR.MINOR.PATCH` convention as usual. Version `0.x.x` indicates the SO:UK Data Centre is not in final production ready state yet. `MINOR` version is bumped only if there's major functional improvement to the user experience, for example, when CVMFS is deployed. Otherwise, it is always a `PATCH` version release.

:::{warning}
Before making a new release, check Read the Doc in <https://readthedocs.org/projects/souk-data-centre/builds/> to see if the `latest` build is successful first.
:::

`bump-my-version` is used to automatically bump the version string scattered in multiple files. See `pyproject.toml` under `[tool.bumpversion]` for details.

To make a new release,

1. Update the `docs/changelog.md` to includes changes made since last release. GitHub can be useful here: <https://github.com/simonsobs-uk/data-centre/compare/v0.4.1...main>.

2. Make sure there's no uncommitted changes.

3. Run

    - `make bump PART=patch` for patch release,
    - `make bump PART=minor` for minor release,
    - `make bump PART=major` for major release.

4. Check Read the Doc at <https://readthedocs.org/projects/souk-data-centre/builds/> to see the new builds are deployed successfully.

## Releasing to `/opt/simonsobservatory` on `vm77`

`make opt`.

## Single file targets

`make man txt` and upload to <https://github.com/simonsobs-uk/data-centre/releases/latest> manually.

TODO: automate this.
