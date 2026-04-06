# File Permissions in Linux

## Project Description

The research team requires updates to file permissions within the `projects` directory, as the current permissions do not reflect the appropriate level of authorization. Updating these permissions ensures that access aligns with security requirements and prevents unauthorized access.

This project demonstrates how Linux commands are used to examine and modify permissions while applying the **principle of least privilege**.

---

## Check File and Directory Details

![Figure 1](figure1_ls-la.png)

The `ls -la` command is used to display a detailed listing of files and directories, including hidden files.

This output shows:

* One directory: `drafts`
* One hidden file: `.project_x.txt`
* Multiple project files

The first column represents the **10-character permission string**, which defines access rights.

---

## Describe the Permissions String

Linux permissions follow this structure:

```
-rw-rw-r--
```

* 1st character → file type (`-` = file, `d` = directory)
* Next 3 → user permissions
* Next 3 → group permissions
* Last 3 → others permissions

Permissions include:

* `r` → read
* `w` → write
* `x` → execute
* `-` → no permission

Example:

* User → read, write
* Group → read, write
* Others → read

---

## Change File Permissions

![Figure 2](figure2_chmod.png)

Command used:

```
chmod o-w project_k.txt
```

This removes write permission from **other users**, preventing unauthorized modification.

The changes are verified using `ls -la`.

---

## Change Permissions on a Hidden File

![Figure 3](figure3_hidden.png)

Command used:

```
chmod u-w,g-w,g+r .project_x.txt
```

This:

* Removes write access from user and group
* Ensures read access for group

Hidden files (starting with `.`) require careful permission handling.

---

## Change Directory Permissions

![Figure 4](figure4_directory.png)

Command used:

```
chmod g-x drafts
```

This removes execute permission from the group, ensuring only the authorized user can access the directory.

---

## Summary

File permissions were reviewed and modified using Linux commands such as `ls -la` and `chmod`. These changes ensure that access is restricted to authorized users only.

Applying the principle of least privilege improves system security and prevents unauthorized access to sensitive files and directories.
