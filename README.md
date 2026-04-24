# Secure Coding Standards

[![Deploy to GitHub Pages](https://github.com/cmu-sei/secure-coding-standards/actions/workflows/deploy.yml/badge.svg)](https://github.com/cmu-sei/secure-coding-standards/actions/workflows/deploy.yml)

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

Look at the [Content documentation](https://content.nuxt.com/) to learn more.

## Setup

### Prerequisites

This project requires **Node.js v22.22.2** (as found in `.nvmrc`). It is recommended to use [nvm](https://github.com/nvm-sh/nvm) to manage Node versions. Use the `.nvmrc` file included in this repository as a source of truth. You can switch to the correct version by running:

```bash
nvm use
```

### 1. Authenticate with GitHub Package Registry

This project depends on a package hosted on GitHub Package Registry (`npm.pkg.github.com`). GitHub requires authentication to install packages from this registry, even public ones. You only need to do this once per machine.

1. Create a GitHub Personal Access Token (PAT):
   - Go to **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**
   - Click **Generate new token (classic)**
   - Give it a name (e.g. `npm read:packages`)
   - Select only the **`read:packages`** scope
   - Click **Generate token** and copy it

2. Add the token to your global npm config (replace `YOUR_GITHUB_PAT` with the token you copied):

   ```bash
   echo "//npm.pkg.github.com/:_authToken=YOUR_GITHUB_PAT" >> ~/.npmrc
   ```

   > **Note:** This writes to `~/.npmrc` (your home directory), not the project's `.npmrc`, so your token is never committed to the repository.

3. If you are on a network that uses SSL inspection (e.g. a corporate proxy), Node.js may fail to verify certificates. Set the `NODE_EXTRA_CA_CERTS` environment variable to point to your organization's CA certificate bundle. Add the following to your shell profile (e.g. `~/.zshenv` or `~/.bash_profile`):

   ```bash
   export NODE_EXTRA_CA_CERTS="/path/to/your/corporate-ca.pem"
   ```

   External contributors on standard networks do not need this step.

### 2. Install dependencies

```bash
npm install
```

## Development Server

Start the development server on http://localhost:3000

```bash
npm run dev
```

## Production

Build the SSG (static site) application for production:

```bash
npm run generate
```

Locally preview production build:

```bash
npm run preview
```

Checkout the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
