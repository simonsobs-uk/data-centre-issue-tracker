(computing-resources)=
# Managing and Maintaining Computing Resources

## New accounts

### New SO:UK VO membership

Go to [VOMS Admin > souk.ac.uk](https://voms.gridpp.ac.uk:8443/voms/souk.ac.uk/admin/home.action) and manage there. 

(new-users)=
### Adding new users on the submit node `vm77`

Point the user to [this section](#obtaining-unix-account) and ask them to send those info to you.

0. If the user ssh key comment contains their email address,
    replace it with something else.
1. Edit `/usr/local/etc/staged/common.yaml` on `vm77`, replace the following `ALL_CAP` variables accordingly,

    ```yaml
    common::users:
      USER_NAME:
        uid: UID
        comment: FIRST_NAME LAST_NAME
        home: /home/USER_NAME
        keys:
          - "ssh-ed25519 KEY_VALUE COMMENT"
        password: "$6$...$..."
        groups:
          - sudo
          - simonsobservatory
    ```

    :::{note}
    For `UID`, increments according to the list. Just make sure it has not been used.

    For `sudo` groups, obviously only grant those you want them to have sudo privillege.
    :::

2. Tell Robert to update.

3. To check if the config is populated, check the file `/etc/passwd` and see if the new users is there. If it does, the user should be ready to go.

:::{warning}
The content of this file contains sensitive information,
such as salted, hashed passwords,
which is configured to be readable only to `root` at `/etc/shadow`.
Hence, the config file `/usr/local/etc/staged/common.yaml` should be treated
with the same level of permission.
:::

(content-manager-registration)=
### Register as a new content manager (CVMFS)

1. Run `ssh northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk` from any computer. Then you'd see something like

        (northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk) Authenticate at
        -----------------
        https://aai.egi.eu/device?user_code=...
        -----------------
        Hit enter when you have finished authenticating

    Follow the link and register there.

2. On <https://aai.egi.eu/auth/realms/egi/account/#/personal-info>, copy the content of "Username" field.

3. Follow [CVMFS - GridPP Wiki](https://www.gridpp.ac.uk/wiki/CVMFS#Request_access) to send an email including the username above as your `voperson_id`:

- Name of the VO or CVMFS repository: `northgrid.gridpp.ac.uk`
- The “voperson_id” from your account in EGI CheckIn: ...@egi.eu

4. Wait for email from <lcg-support@gridpp.rl.ac.uk> when the admin added you to the service.

## Software deployments

(CVMFS-pub)=
### Publishing to CVMFS

See [above](#content-manager-registration) if you haven't applied for the role of content manager yet.

Then

```sh
ssh northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk
```

The recommended ssh config is:

```
Host cvmfs
    HostName cvmfs-upload01.gridpp.rl.ac.uk
    User northgridsgm
    ControlPath ~/.ssh/control-%r@%h:%p
    ControlMaster auto
    ControlPersist yes
```

Then starts to write something in `~/cvmfs_repo/simonsobservatory`. What you write will immediately be available at `/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory` on this publishing node. But it will only be synchronized to other sites with a time scale of around 2.5-3 hours.

On `vm77`, check if you see your stuffs is in `/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory` already, if so, you can start to submit jobs that reads from there.

## Monitoring

### `condor_status`

See [condor_status — HTCondor Manual](https://htcondor.readthedocs.io/en/latest/man-pages/condor_status.html) for details.

`sudo condor_status`
: list all nodes in the pool along with their basic status information

`sudo condor_status -long`
: for more detailed information about each node

`sudo condor_status -constraint 'Arch == "x86_64"'`
: see available nodes after constraints

`condor_status -avail`
: Lists available nodes

`sudo condor_status -format "%s\n" Machine | sort -u`
: Lists only the machine names

`sudo condor_status -autoformat Machine Arch Microarch | sort -u`
: Auto-format instead.
