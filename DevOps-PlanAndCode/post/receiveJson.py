import json
import request

from planCodeAPI import planCodeAPI




TEST_JSON_RES = '''{  "$schema": "http://json-schema.org/draft-04/schema#",
       "title": "Response information",
       "type": "object",
       "description": "Contains operation(method) and its execution status with description",
       "properties": {
         "object_type": "tmp",
         "operation": "Build",
         "status": "TRUE",
         "description": "tmp",
         "project_name": "son",
		 "user_id": "gtusoftware2017",
		 "user_pass": "software2017",
		 "repository_url": "www.github.com/GtuDevOps/son",
         "method_name" : "move"
       }
}'''


def main_function(json_file):
	split_str = TEST_JSON_RES.split(',') #sys.argv[1].split(',')
	operation = ""
	status = ""
	description = ""
	project_name = ""
	user_id = ""
	user_pass = ""
	repository_url = ""
	method_name = ""

	for x in range(0, 13):
		if "operation" in split_str[x]:
			operation = split_str[x].strip()
			operation = operation.replace("operation","").replace(":","").replace('"','').replace(" ","")

		if "status" in split_str[x]:
			status = split_str[x].strip()
			status = status.replace("status","").replace(":","").replace('"','').replace(" ","")

		if "description" in split_str[x]:
			description = split_str[x].strip()
			description = description.replace("description","").replace(":","").replace('"','').replace(" ","")

		if "project_name" in split_str[x]:
			project_name = split_str[x].strip()
			project_name = project_name.replace("project_name","").replace(":","").replace('"','').replace(" ","")

		if "user_id" in split_str[x]:
			user_id = split_str[x].strip()
			user_id = user_id.replace("user_id","").replace(":","").replace('"','').replace(" ","")

		if "user_pass" in split_str[x]:
			user_pass = split_str[x].strip()
			user_pass = user_pass.replace("user_pass","").replace(":","").replace('"','').replace(" ","")

		if "repository_url" in split_str[x]:
			repository_url = split_str[x].strip()
			repository_url = repository_url.replace("repository_url","").replace(":","").replace('"','').replace(" ","")
			repository_url = repository_url.split("/")[1]

		if "method_name" in split_str[x]:
			method_name = split_str[x].strip()
			method_name = method_name.replace("method_name","").replace(":","").replace('"','').replace(" ","")


	print("LOGIN: " + user_id + " " + user_pass + " " + repository_url)
	pc=planCodeAPI(user_id, user_pass, repository_url)
	print("SELECTING PROJECT: " + project_name)
	pc.chooseProject(project_name)


main_function(TEST_JSON_RES)
