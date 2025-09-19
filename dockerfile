# devbox: Ubuntu 24.04 + GitHub CLI, Node 20, Gemini CLI, Claude Code, Cursor CLI, OpenAI Codex, code-server
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-lc"]

# Basics
RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates curl wget git unzip zip gnupg lsb-release sudo \
  openssh-client bash-completion python3 python3-pip python3-venv build-essential pkg-config \
  && rm -rf /var/lib/apt/lists/*

# Node.js 20 (multi-arch via NodeSource) 
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
  && apt-get install -y nodejs && node -v && npm -v
# (NodeSource publishes arm64/amd64 builds.) :contentReference[oaicite:3]{index=3}

# GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
   | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
   chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && \
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
   > /etc/apt/sources.list.d/github-cli.list && \
   apt-get update && apt-get install -y gh && rm -rf /var/lib/apt/lists/*
# (Official gh repo.) :contentReference[oaicite:4]{index=4}

# Gemini CLI (official)
RUN npm install -g @google/gemini-cli
# (Open-source CLI by Google.) :contentReference[oaicite:5]{index=5}

# Claude Code (official)
RUN npm install -g @anthropic-ai/claude-code
# (Anthropic’s terminal coding agent.) :contentReference[oaicite:6]{index=6}

# Cursor CLI (terminal tool; not the GUI editor)
RUN curl -fsS https://cursor.com/cli | bash || true \
 && if [ -d "/root/.cursor/bin" ]; then cp /root/.cursor/bin/* /usr/local/bin/; fi
# (CLI installer & docs.) :contentReference[oaicite:7]{index=7}

# OpenAI Codex (official CLI tool)
RUN npm install -g @openai/codex
# (Official OpenAI Codex CLI as documented in INSTALLATION.md)

# code-server (VS Code in the browser)
ENV CODE_SERVER_PORT=8080
RUN curl -fsSL https://code-server.dev/install.sh | sh
# (Official install script.) :contentReference[oaicite:8]{index=8}
EXPOSE 8080

# Shell QoL
RUN echo 'if [ -f /usr/share/bash-completion/bash_completion ]; then . /usr/share/bash-completion/bash_completion; fi' >> /etc/bash.bashrc
WORKDIR /workspace

RUN ln -sf /usr/bin/code-server /usr/local/bin/code
# No default CMD (we’ll choose in Compose: code-server or bash)
# Make 'code' resolve to code-server (you already have this)
RUN ln -sf /usr/bin/code-server /usr/local/bin/code

# QoL: declare a canonical workspace path (helps tooling & compose defaults)
ENV WORKSPACE=/workspace
VOLUME ["/workspace"]
