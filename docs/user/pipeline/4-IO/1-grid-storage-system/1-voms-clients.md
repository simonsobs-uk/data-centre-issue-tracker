(setup-voms-clients)=
# Setting up VOMS Clients

If you work on machines supported by us, you can skip this part. This part needed to be done once per machine.

## Installing the clients

You would need to install VOMS Clients by following the instruction in the [VOMS Clients guide](https://italiangrid.github.io/voms/documentation/voms-clients-guide/3.0.5/#installing-the-clients-). The currently supported OS is either RHEL 6/7 or Debian 6 as of writing:

```bash
# RHEL
sudo yum install voms-clients-java
# Debian
sudo apt-get install voms-clients3
```

## Configuring VOMS trust anchors

Create these paths with the corresponding contents below:

```sh
# generated by running
# head /etc/grid-security/vomsdir/souk.ac.uk/*
==> /etc/grid-security/vomsdir/souk.ac.uk/voms02.gridpp.ac.uk.lsc <==
/C=UK/O=eScience/OU=Oxford/L=OeSC/CN=voms02.gridpp.ac.uk
/C=UK/O=eScienceCA/OU=Authority/CN=UK e-Science CA 2B

==> /etc/grid-security/vomsdir/souk.ac.uk/voms03.gridpp.ac.uk.lsc <==
/C=UK/O=eScience/OU=Imperial/L=Physics/CN=voms03.gridpp.ac.uk
/C=UK/O=eScienceCA/OU=Authority/CN=UK e-Science CA 2B

==> /etc/grid-security/vomsdir/souk.ac.uk/voms.gridpp.ac.uk.lsc <==
/C=UK/O=eScience/OU=Manchester/L=HEP/CN=voms.gridpp.ac.uk
/C=UK/O=eScienceCA/OU=Authority/CN=UK e-Science CA 2B
```

## Configuring VOMS server endpoints

Create these paths with the corresponding contents below:

```sh
# generated by running
# head /etc/vomses/* 
==> /etc/vomses/souk.ac.uk-voms02.gridpp.ac.uk <==
"souk.ac.uk" "voms02.gridpp.ac.uk" "15519" "/C=UK/O=eScience/OU=Oxford/L=OeSC/CN=voms02.gridpp.ac.uk" "souk.ac.uk" "24"

==> /etc/vomses/souk.ac.uk-voms03.gridpp.ac.uk <==
"souk.ac.uk" "voms03.gridpp.ac.uk" "15519" "/C=UK/O=eScience/OU=Imperial/L=Physics/CN=voms03.gridpp.ac.uk" "souk.ac.uk" "24"

==> /etc/vomses/souk.ac.uk-voms.gridpp.ac.uk <==
"souk.ac.uk" "voms.gridpp.ac.uk" "15519" "/C=UK/O=eScience/OU=Manchester/L=HEP/CN=voms.gridpp.ac.uk" "souk.ac.uk" "24"
```

(user-credentials)=
# User credentials

This part needed to be done once per machine.

You need to have your grid certificate `certBundle.p12` ready that you obtained from [this section](#obtaining-grid-cert). Then run

```bash
mkdir -p "$HOME/.globus/"
mv certBundle.p12 "$HOME/.globus/usercred.p12"
chmod 600 "$HOME/.globus/usercred.p12"
```

(creating-a-proxy)=
# Creating a proxy

This part needed to be done periodically.

```bash
voms-proxy-init --voms souk.ac.uk --valid 168:0
```

> The command `voms-proxy-init` is used to contact the VOMS server and retrieve an Attribute Certificate (AC) containing user attributes that will be included in the proxy certificates.

The Attribute Certificate (AC) is configured with a maximum validity of 168 hours (7 days).

Example output after running this command will be:

```
❯ voms-proxy-init --voms souk.ac.uk --valid 168:0
Enter GRID pass phrase for this identity:
Contacting voms03.gridpp.ac.uk:15519 [/C=UK/O=eScience/OU=Imperial/L=Physics/CN=voms03.gridpp.ac.uk] "souk.ac.uk"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u$UID.

Your proxy is valid until Tue Nov 14 08:45:38 GMT 2023
```

The path `/tmp/x509up_u$UID` will be useful later. You can also run `voms-proxy-info --all` and see it again in the `path` attributes.