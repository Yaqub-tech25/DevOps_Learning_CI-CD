# Assignment 02: Container Delivery with GitHub Actions

## Goal

Package the calculator from Assignment 01 as a Docker image and automatically publish it to GitHub Container Registry (GHCR) after the CI checks pass.

## Delivery flow

1. A push to `main` starts the existing lint and unit-test job.
2. If those checks pass, the container publishing job builds the image from `Dockerfile`.
3. The workflow authenticates to GHCR with the repository's `GITHUB_TOKEN` and publishes the image with `main` and commit-SHA tags.
4. Pull requests run CI, but do not publish an image.

The publishing job needs only the `packages: write` permission. No Docker Hub account or manually configured secret is required.

The image name is `ghcr.io/yaqub-tech25/devops_learning_ci-cd`. After the workflow publishes it, the latest main-branch image can be pulled with:

```bash
docker pull ghcr.io/yaqub-tech25/devops_learning_ci-cd:main
```

For a personal GitHub account, a new package starts private. Authenticate to `ghcr.io` before pulling unless you change the package visibility. If you want anyone to pull the image without signing in, you can make it public under the package's **Package settings**. GitHub does not let a public package be changed back to private, so choose that visibility deliberately.

## Build and run locally

Run these commands from the repository root:

```bash
docker build -f Assignment-02-CD/Dockerfile -t calculator-cd .
docker run --rm calculator-cd
```

Expected output:

```text
Calculator container is running
2 + 3 = 5
10 - 4 = 6
```

## Files

- `Dockerfile` packages the calculator app and its small runnable entry point.
- `main.py` runs the existing add and subtract functions.
- `.github/workflows/ci.yml` runs CI first, then publishes the image only after successful checks on `main`.

## Learning outcomes

- Building a Docker image from application code.
- Publishing a versioned container image with GitHub Actions.
- Using `GITHUB_TOKEN` and least-privilege package permissions.
- Making image publishing depend on successful CI checks.
