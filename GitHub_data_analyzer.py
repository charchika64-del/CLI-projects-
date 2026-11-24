import requests
base_url ="https://api.github.com"
endpoints = {
    "user": "https://api.github.com/users/{username}",
    "repos": "https://api.github.com/users/{username}/repos", #returns list of repositories
    "commit": "https://api.github.com/repos/{username}/{repo}/commits/{commit_id}",
    "repo_detail": "https://api.github.com/repos/{username}/{repo}", #returns details of one repository
    "contents": "https://api.github.com/repos/{username}/{repo}/contents/"
}
    
def user_info(username):
    all_repos = []
    
    user_url = endpoints["user"].format(username=username)
    response = requests.get(user_url,timeout=5)
    response.raise_for_status()
    data = response.json()
    print("Name_",data['name'])
    print("Login_",data['login'])
    print("ID_",data['id'])    
    print("Bio_",data['bio'])
    print("HTML url_",data['html_url'])
    print("Location_",data['location'])
    print("Email_",data['email'])
    print("Followers_",data['followers'])
    print("Following_",data['following'])
    
    repo_url = endpoints["repos"].format(username=username)
    repo_data = requests.get(repo_url,timeout=5)
    repo_data.raise_for_status()
    repo_data = repo_data.json()
    for repo in repo_data:
        all_repos.append(repo['name'])
    print(f"Public Repositories_ {data['public_repos']} {all_repos}")
    
    
def repo_detailed_info(username):
    repo = input("Enter repo name_ ")
    repo_url = endpoints["repo_detail"].format(username=username,repo=repo)
    response = requests.get(repo_url,timeout=5)
    response.raise_for_status()
    repository = response.json()
    print("Name_",repository['name'])
    print("Language_",repository['language'])
    print("Watchers_",repository['watchers'])
    print("Stargazers_",repository['stargazers_count'])
    print("Html url_",repository['html_url'])
    print("Forks_",repository["forks"])
    print("Size",repository["size"])
     
    print("Files in the repository –")
    content_url = endpoints["contents"].format(username=username,repo=repo)
    response = requests.get(content_url,timeout=5)
    response.raise_for_status()
    file_list = response.json()
    for items in file_list:
        print(items["name"])    

                
def know_commit_message(username):
    commit_id = input("Enter commit id_ ")
    repo = input("Enter repo name_ ")
    url = endpoints["commit"].format(username=username,repo=repo,commit_id=commit_id)
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    data = response.json()
    print("Commit Message",data['commit']['message'])
    
    
def list_repo(username):
    url = endpoints["repos"].format(username=username)
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    repositories_list = response.json()
    for repositories in repositories_list:
        name = repositories['name']
        html_url = repositories['html_url']
        print(f"Name {name} Url {html_url}")
    

print("Type 1 to get information about the user.")
print("Type 2 to get a specific repository's detail.")
print("Type 3 to get commit message based on commit id.")
print("Type 4 to see a list of all repositories by a user.")
print("Type 5 to exit.")

operations = {1:user_info,2:repo_detailed_info,3:know_commit_message,4:list_repo}

while True:
    try:
        choice = int(input("Enter a number"))
        if choice in operations:
            username = input("Enter username_ ")
            operations[choice](username)         
        elif choice == 5:
            break
        else:
            print("This number is not valid")
    except ValueError:
            print("Type a number")
    except requests.exceptions.Timeout:
            print("The request is taking time")
    except requests.exceptions.HTTPError as e:
            print("HTTP Error",e)
    except requests.exceptions.ConnectionError:
            print("Please chaeck your network")
