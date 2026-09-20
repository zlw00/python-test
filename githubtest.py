from os import mkdir
from pathlib import Path
from sys import excepthook

import requests
import json


def get_username():
    while True:
        username = input("请输入github用户名：").strip()
        if username == "":
            print("输入的用户名为空，请重新输入")
        return username


def fetch_github_user(username):
    """请求github api，捕获各类网络/请求异常，返回用户字典"""
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def show_user_summary(user):
    """解析并打印用户信息，name和bio做默认值处理"""
    login = user["login"]
    name = user.get("name") or "暂无"
    bio = user.get("bio") or "暂无"
    public_repos = user["public_repos"]
    followers = user["followers"]
    html_url = user["html_url"]
    created_at = user["created_at"]
    print("\n用户名：", login)
    print("姓名：", name)
    print("简介：", bio)
    print("公开仓库数：", public_repos)
    print("关注者数：", followers)
    print("主页：", html_url)
    print("创建时间：", created_at)


def save_user_data(username, user):
    """保存完整json到data目录，目录不存在自动创建"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    output_path = data_dir / f"{username}.json"
    output_path.write_text(json.dumps(user, ensure_ascii=False, indent=4), encoding="utf-8")
    print(f"查询结果已保存到{output_path}")


def should_continue():
    """询问是否继续查询"""
    while True:
        user_in = input("是否继续查询(y/n)?")
        if user_in == "y":
            return True
        elif user_in == "n":
            return False
        else:
            print("输入错误，请重新输入")


def main():
    print("====github用户信息查询器====")
    try:
        while True:
            username = get_username()
            print("正在查询......")
            user_data = fetch_github_user(username)
            if user_data is None:
                print("用户不存在，或请求失败，请检查用户名和网络。")
            else:
                print("用户信息如下：")
                show_user_summary(user_data)
                print("正在保存....")
                save_user_data(username, user_data)

            if not should_continue():
                print("程序退出!")
                break
    except KeyboardInterrupt:
        print("\n\n你按下了 Ctrl+C，程序安全退出")


if __name__ == "__main__":
    main()
