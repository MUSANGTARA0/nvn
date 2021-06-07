import os, sys, pathlib

foldername = input("Project Name: ")

p = pathlib.Path(foldername).mkdir(parents=True, exist_ok=True)
p = pathlib.Path(foldername + "/" + ".nvnfile").mkdir(parents=True, exist_ok=True)

nvn_json = open(f"{foldername}/nvn.json", "w")
nvn_config = open(f"{foldername}/.nvnfile/config.nvn.json", "w").write("{}")
nvn_plugin = open(f"{foldername}/.nvnfile/plugins.nvn.json", "w").write("{}")
nvn_cache = open(f"{foldername}/.nvnfile/cache.nvn.json", "w").write("{}")

nvn_json.write('')
nvn_json.close()