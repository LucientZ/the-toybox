# Overview

Because I am a human being, I will forget how things work here.

Useful packer commands to do in neovim (From packer docs):

```shell
# You must run this or `PackerSync` whenever you make changes to your plugin configuration
# Regenerate compiled loader file
:PackerCompile

# Remove any disabled or unused plugins
:PackerClean

# Clean, then install missing plugins
:PackerInstall

# Clean, then update and install plugins
# supports the `--preview` flag as an optional first argument to preview updates
:PackerUpdate

# Perform `PackerUpdate` and then `PackerCompile`
# supports the `--preview` flag as an optional first argument to preview updates
:PackerSync

# Show list of installed plugins
:PackerStatus

# Loads opt plugin immediately
:PackerLoad completion-nvim ale