Moodle on OpenShift
===================

This git repository helps you get up and running quickly w/ a Moodle installation on OpenShift.  

Running on OpenShift
----------------------------

Create an account at https://www.openshift.com and install the client tools (run 'rhc setup' first)

Create a php-5.4 application (you can call your application whatever you want)

    rhc app create moodle php-5.4 postgresql9.2 --from-code=https://github.com/nuddelaug/openshift-moodle-example.git

That's it, you can now checkout your application at:

    http://moodle-$yournamespace.rhcloud.com

Moodle is being setup already during the deployment phase so ensure you'll update the items of interesst:

    * fullname of your site 
    * shortname of your site

the default administrative credentials equal the Database credentials. Please ensure to create your own administrative User.

Notes
=====

GIT_ROOT/.openshift/action_hooks/deploy:
    This script is executed with every 'git push'.  Feel free to modify this script
    to learn how to use it to your advantage.  By default, this script will create
    the database tables that this example uses.

    If you need to modify the schema, you could create a file
    GIT_ROOT/.openshift/action_hooks/alter.sql and then use
    GIT_ROOT/.openshift/action_hooks/deploy to execute that script (make sure to
    back up your application + database w/ 'rhc app snapshot save' first :) )
