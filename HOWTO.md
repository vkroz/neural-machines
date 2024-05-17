
# How To


## HuggingFace

Login to HF: `huggingface-cli login`

Test ssh git access with Huggingface
```shell
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
ssh -T git@hf.co
```

Clone repo: `git clone git@hf.co:/$HF_USERNAME/$REPO_NAME`

Enable large files in the repo
```shell
git lfs install
huggingface-cli lfs-enable-largefiles .
```

## Building documentation

Framework for building online book: 
https://jupyterbook.org/en/stable/intro.html
