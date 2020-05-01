# instructions from Coursera

<https://learner.coursera.help/hc/en-us/articles/360004990332-Download-Jupyter-Workspace-files>

If you’ve completed Jupyter notebook assignments in a Coursera course, you can download your files so you can run them locally once the course ends. Your files will not stay on Coursera indefinitely, so you'll need to download them if you want to keep them.


## Download Jupyter Workspace files


Download Jupyter Workspace files



### Download a single notebook

To **download a single notebook**:

Open the notebook you want to download
Click **File**
Click **Download As**
Choose a file format, then download your notebook.

### Download all of your notebooks at the same time

To download all of your Jupyter Workspace files at the same time:

1. Launch one of your notebooks from coursera.org
2. In the upper right, click the Coursera logo
3. You'll see a file view page that lists all Jupyter resources in your current course. Click the **New**, then select **Terminal** to open the system command line.
4. You'll see a shell prompt open. In the shell prompt, type or paste the following statements:

+  Remove the previous archive, if it exists:
```sh
rm -f ~/workspace.tar.gz && rm  -f ~/work/workspace.tar.gz
```


+   Create a zipped archive of your workspace directory:
```sh
 tar -czf ~/workspace.tar.gz ~/work
```

 * Move the archive into the workspace directory so you can see it: 
```sh
mv ~/workspace.tar.gz ~/work/workspace.tar.gz
```

5. Once the commands run successfully, click on the ‘Coursera’ logo again to return to the file view.
6. In the file view, select **workspace.tar.gz**, then click **Download**. Your browser will download the workspace archive, which is yours to keep.
7. Remove the archive file: 
```sh
rm ~/work/workspace.tar.gz*
```

**Note:** If your zip file is larger than 100MB, you will need to split it up into smaller files instead and download each of them, using the following commands:
```sh
tar -czf - ~/work | split --bytes=100MB - ~/workspaces.tar.gz
mv ~/workspace.tar.gz* ~/work/
```