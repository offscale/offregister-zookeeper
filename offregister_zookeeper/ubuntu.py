# -*- coding: utf8 -*-

from offregister_fab_utils import Package
from offregister_fab_utils.apt import apt_depends


def install(c, *args, **kwargs):
    version = "3.4.5"
    apt_depends(
        c,
        Package(name="zookeeper", version=version),
        Package(name="zookeeperd", version=version),
    )

    # /etc/zookeeper/conf/zoo.cfg
    """$ tree /etc/zookeeper/conf
       ├── configuration.xsl
       ├── environment
       ├── log4j.properties
       ├── myid
       └── zoo.cfg"""

    return "zookeeper installed"


def serve(c, *args, **kwargs):
    if c.run("service zookeeper status") == "zookeeper stop/waiting":
        c.sudo("service zookeeper start")
