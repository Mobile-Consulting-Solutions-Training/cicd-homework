# CI/CD Homework

A small FastAPI application with a GitHub Actions pipeline that tests, builds a Docker image, and publishes it to GitHub Container Registry (GHCR) on every push to `main`.

```text
Push to GitHub
      |
Run automated tests (pytest)
      |
Build Docker image
      |
Push image to GHCR
```

## Pipeline Runs

Two pipeline runs, both completed successfully - view them live in the [Actions tab](../../actions).

### Run 1 - `Create CI/CD application` (v1.0.0)

Commit `68c06e6` · [View run](../../actions/runs/35127261914)

```text
✓ test-build-publish in 25s
  ✓ Set up job
  ✓ Checkout repository
  ✓ Set up Python
  ✓ Install dependencies
  ✓ Run tests
  ✓ Log in to GitHub Container Registry
  ✓ Compute lowercase image name
  ✓ Build Docker image
  ✓ Push Docker image
  ✓ Complete job
```

### Run 2 - `Release version 2.0` (v2.0.0)

Commit `0b8a13c` · [View run](../../actions/runs/35127425817)

```text
✓ test-build-publish in 29s
  ✓ Set up job
  ✓ Checkout repository
  ✓ Set up Python
  ✓ Install dependencies
  ✓ Run tests
  ✓ Log in to GitHub Container Registry
  ✓ Compute lowercase image name
  ✓ Build Docker image
  ✓ Push Docker image
  ✓ Complete job
```

## Verified Deployments

Both CI-published images were pulled and run locally, hitting the live endpoint to confirm the version actually deployed matched the version actually published:

**v1.0.0** (from `ghcr.io/ajmobileconsulting/cicd-homework@sha256:ccc66b5cbc5e39e406d463f6755a56453771b1f686cb01e3d763cb208fe4365a`):
```text
$ curl -s http://localhost:8111
{"application":"CI/CD Homework","version":"1.0.0"}
```

**v2.0.0** (current `:latest`):
```text
$ curl -s http://localhost:8111
{"application":"CI/CD Homework","version":"2.0.0"}
```

## Running It Yourself

```bash
docker pull ghcr.io/ajmobileconsulting/cicd-homework:latest
docker run -d --name cicd-homework -p 8111:8111 ghcr.io/ajmobileconsulting/cicd-homework:latest
curl http://localhost:8111
```

## Note on Repo History

This repository was originally created under the personal `ajMobileConsulting` account, then transferred into the `Mobile-Consulting-Solutions-Training` org - the container images published above are still under the pre-transfer GHCR namespace (`ghcr.io/ajmobileconsulting/...`), since GHCR packages don't automatically move with a repo transfer. The next push to `main` will publish under the org's namespace instead.

## Environment Note

The workflow's `Compute lowercase image name` step is a deliberate deviation from a "generic" version of this pipeline: `${{ github.repository }}` can resolve to a mixed-case owner/repo path (as it did here, under `ajMobileConsulting`), but GHCR/Docker image tags must be all-lowercase - that step normalizes it before the build/push steps run.
