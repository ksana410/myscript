#!/bin/bash

# add default values
XMR_CFG_FILE=/xmr/nanominer/config.ini
RUN_FILE=/xmr/run
RIGNAME=$(cat /dev/urandom | head -n 10 | md5sum | head -c 10)

if [[ ! -f ${RUN_FILE} ]]
then
# init config file
    if [[ -z ${Wallet} ]]
    then
        echo "init default config ..."
        rm ${XMR_CFG_FILE}
        cp /xmr/defconfig.ini ${XMR_CFG_FILE}
        sed -i "s/RigName/${RIGNAME}/g" ${XMR_CFG_FILE}
    else
        echo "init config ..."
        sed -i "s/Wallet/${Wallet}/g" ${XMR_CFG_FILE}
        sed -i "s/RigName/${RigName}/g" ${XMR_CFG_FILE}
        sed -i "s/Email/${Email}/g" ${XMR_CFG_FILE}
    fi
# generating a run file
    cat ${XMR_CFG_FILE} > ${RUN_FILE}
else
    echo "init xmr..."
fi

# start xmr
exec /xmr/nanominer/nanominer ${XMR_CFG_FILE}