#!/bin/bash

# add default values
XMR_CFG_FILE=/xmr/nanominer/config.ini
RIGNAME=$(cat /dev/urandom | head -n 10 | md5sum | head -c 10)

# init config file
if [[ -z ${Wallet} ]]
then
    echo "init default config ..."
    rm ${XMR_CFG_FILE}
    cp /xmr/defconfig.ini ${XMR_CFG_FILE}
    echo "init default config: ${XMR_CFG_FILE}"
    sed -i "s/RigName/${RIGNAME}/g" ${XMR_CFG_FILE}
else
    echo "init config ..."
    sed -i "s/Wallet/${Wallet}/g" ${XMR_CFG_FILE}
    sed -i "s/RigName/${RigName}/g" ${XMR_CFG_FILE}
    sed -i "s/Email/${Email}/g" ${XMR_CFG_FILE}
fi

# show Wallet and RigName ...
cat ${XMR_CFG_FILE}

# start xmr
exec /xmr/nanominer/nanominer ${XMR_CFG_FILE}