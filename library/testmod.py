#!/usr/bin/python3

ANSIBLE_METADATA = {
        'metadata+version': '1.1',
        'status': ['preview'],
        'supported_by': 'offsecgraham'

    }

DOCUMENTATION = '''
---
module: testmod
short_description: This module is being designed so we can observe the minium required config for an Ansible module.
description:
    - user passes a param called 'name' <str> <required>
    - user passes a param called 'argument' <bool>
    - if argument: tru then ansible returns name + additional string as well as indicationg a YELLOW CHANGE in the play recap
    - if argument: false then ansible returns name string and indicates GREEN OK in the play recap
    - if "name: fail me" then ansible returns FAILED in play recap
author:
    - offsecgraham@gmail.com
'''

EXAMPLE = '''
# pass in a name
- name: requesting a FREEN OK from our new module
  testmod:
    name: Glenn
    agument: false

- name: requesting a YELLOW CHANGE from our new module
  testmod:
    name: Glenn
    argument: true

- name: requesting a RED FAIL from our new module
  testmod:
    name: fail me
'''

RETURN = '''
original_message:
    description: The name parameter that was originally passed by the user
    type: str
message:
    description: the name parameter changed or argument in some fashion
    type: str
'''

from anisble.module_utils.basic import AnsibleModule

def run_module():
    """ module logic"""
    module_args= dict(
            name=dict(type='str', required=True),
            argument=dict(type='bool', required=False)
            #ipaddress=dist(type='list', required=False),
        )

    ## see the result dictionary object
    ## we primarly care about the change and state
    ## change is if hte module effectively modified the target
    ## result contains all of the KEYS you want to return after you module completes
    results = dict(
            changed=False,
            original_message='',
            message='')

    module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True)

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']

    if module.params['argument'] == False:
        result['message'] = module.params['name']

    else:
        result['message'] = module.params['name'] + " is a wild and crazy guy!!! or so says Dan Akroyd."
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg="You requested me to fail!", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == "__main__":
    main()

    ##




