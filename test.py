# import googleapiclient.discovery
#
#
# def get_policy(project_id, version=1):
#     """Gets IAM policy for a project."""
#
#     # credentials = service_account.Credentials.from_service_account_file(
#     #     filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
#     #     scopes=["https://www.googleapis.com/auth/cloud-platform"],
#     # )
#     service = googleapiclient.discovery.build("cloudresourcemanager", "v1")
#     policy = (
#         service.projects()
#             .getIamPolicy(
#             resource=project_id,
#             body={"options": {"requestedPolicyVersion": version}},
#         )
#             .execute()
#     )
#     print(policy)
#     return policy
#
#
# def modify_policy_remove_member(policy, role, member):
#     """Removes a  member from a role binding."""
#     binding = next(b for b in policy["bindings"] if b["role"] == role)
#     print(binding)
#     # if "members" in binding and member in binding["members"]:
#     #     binding["members"].remove(member)
#     # print(binding)
#     # return policy
#
#
# if __name__ == '__main__':
#     policy = get_policy('gcp-project')
#
# import googleapiclient.discovery
#
#
# def secops(request):
#     print("Inside cloud function")
#     project_id = request.get_json().get('project_id')
#     print(project_id)
#     members = request.get_json().get('member')
#     method = request.get_json().get('method')
#     if method == "add":
#         for member in members:
#             policy = get_policy(project_id)
#             role = request.get_json().get('role')
#             added_member_policy = modify_policy_add_role(policy, role, member)
#             new_policy = set_policy(project_id, added_member_policy)
#             print(new_policy)
#         return '{"status":"200", "data": "OK"}'
#     if method == "remove":
#         for member in members:
#             policy = get_policy(project_id)
#             removed_member_policy = remove_member(policy, member)
#             new_policy = set_policy(project_id, removed_member_policy)
#             print(new_policy)
#         return '{"status":"200", "data": "OK"}'
#
#
# def get_policy(project_id, version=1):
#     service = googleapiclient.discovery.build("cloudresourcemanager", "v1")
#     policy = (
#         service.projects().getIamPolicy(
#             resource=project_id,
#             body={"options": {"requestedPolicyVersion": version}},
#         ).execute()
#     )
#     return policy
#
#
# def modify_policy_add_role(policy, role, member):
#     """Adds a new role binding to a policy."""
#     binding = {"role": role, "members": [member]}
#     policy["bindings"].append(binding)
#     print(policy)
#     return policy
#
#
# def remove_member(policy, member):
#     for binding in policy['bindings']:
#         if "members" in binding and member in binding["members"]:
#             binding["members"].remove(member)
#             print("Removed the", member)
#     return policy
#
#
# def set_policy(project_id, policy):
#     """Sets IAM policy for a project."""
#     service = googleapiclient.discovery.build(
#         "cloudresourcemanager", "v1")
#
#     policy = (
#         service.projects().setIamPolicy(resource=project_id, body={"policy": policy})
#             .execute()
#     )
#     print(policy)
#     return policy
#
# import json
#
# with open('credentials\credentials.json') as f:
#     d = json.load(f)
#     print(d)
import re


def main():
    # testlist=[]
    # regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    # list1 = ['&^AA', '#$%!', '(*)~', "'}{[]","abhi"]
    # # print([c for entry in list1 for c in entry if not (c.isalpha() or c.isdigit() or c == ' ')])
    # for entry in list1:
    #     if not (regex.search(entry) is None):
    #         testlist.append(True)
    #     else:
    #         testlist.append(False)
    # print(testlist)
    # testlist = ['Akshy','Ashish','Ravi','Ranjan']
    # print([x.isalnum() for x in testlist])
    pdfstr = 'RMD4-188-virtual_machines.pdf'
    # pdfstr = blob.name
    print(pdfstr[:pdfstr.rindex('-')])

if __name__== '__main__':
    main()
