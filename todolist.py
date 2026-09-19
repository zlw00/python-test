import json
from pathlib import Path

TODO_FILE = Path("todos.json")


def load_todos():
    if not TODO_FILE.exists():
        return []
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        print("todolist 文件损坏")
        return []



def save_todos(todos):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)


def show_todos(todos):
    """展示待办列表"""
    print("\n====== 待办清单 ======")
    if len(todos) == 0:
        print("暂无待办")
        return
    for id, item in enumerate(todos, start=1):
        mark = "[x]" if item["done"] else "[ ]"
        print(f"{id}. {mark} {item['title']}")


def add_todo(todos):
    str = input("请输入待办内容")
    str = str.strip()
    if not str:
        print("待办内容不能为空")
        return
    new_item = {
        "title": str,
        "done": False,
    }
    todos.append(new_item)
    save_todos(todos)
    print(f"已添加：{str}")


def complete_todo(todos):
    num = input("请输入待办编号")
    try:
        num = int(num)
    except ValueError:
        print("待办编号必须是整数")
        return
    index = num - 1
    if index < 0 or index>=len(todos):
        print(f"待办编号不存在，请输入1到{len(todos)}的编号")
        return
    if  todos[index]["done"]:
        print("该事项已经完成")
        return

    todos[index]["done"] = True
    save_todos(todos)
    print("修改完成")

def delete_todo(todos):
    show_todos(todos)
    num_str = input("输入要删除的待办编号")
    try:
        num = int(num_str)
    except ValueError:
        print("编号必须是数字！")
        return

    index = num - 1
    if index < 0 or index >= len(todos):
        print(f" 请输入 1 到 {len(todos)} 之间的编号")
        return
    todo = todos[index]
    ans = input(f"确定删除{todo['title']}吗？(y/n)").strip().lower()
    if ans == "y":
        todos.pop(index)
        save_todos(todos)
        print("已经删除")
    else:
        print("取消删除")

def update_todo(todos):
    show_todos(todos)
    num = input("输入要修改的待办编号")
    try:
        num = int(num)
    except ValueError:
        print("待办编号输入错误")
        return
    index = num - 1
    if index < 0 or index >= len(todos):
        print(f"待办编号请输入1-{len(todos)}之间的数字")
        return
    if todos[index]["done"]:
        ans = input("该编号的待办已经完成，是否继续继续修改？(y/n)").strip().lower()
        if ans == "y":
            todos[index]["done"] = False
    new_title = input("输入你要修改待办的内容")
    if not new_title:
        print("修改内容不能为空")
        return
    todos[index]["title"] = new_title
    save_todos(todos)
    print("修改成功")
    show_todos(todos)


def show_done_false(todolist):
    '''展示未完成的待办清单'''

    todolist_false = []
    for todo in todolist:
        if not todo["done"]:
            todolist_false.append(todo)

    if len(todolist_false) <=0:
        print("没有未完成的待办清单")
        return

    for id, item in enumerate(todolist_false, start=1):
        print(f"{id}. [ ] {item['title']}")

def main():
    todolist = load_todos()
    while True:
        print('====== 我的待办清单 ======')
        print('1. 查看待办')
        print('2. 新增待办')
        print('3. 标记完成')
        print('4. 删除待办')
        print('5. 更新待办清单')
        print('6. 展示未完成的待办')
        print('7. 退出')
        userinput = input("请输入操作").strip()
        if userinput == "1":
            show_todos(todolist)
        elif userinput == "2":
            add_todo(todolist)
        elif userinput == "3":
            complete_todo(todolist)
        elif userinput == "4":
            delete_todo(todolist)
        elif userinput == "5":
            update_todo(todolist)
        elif userinput == "6":
            show_done_false(todolist)
        elif userinput == "7":
            print('待办已保存，再见！')
            break
        else:
            print('输入错误，请重新输入')

if __name__ == "__main__":
    main()

# 做一个“命令行待办清单（Todo CLI）”。它不需要图形界面，在终端运行即可。
#
#   最终使用效果：
#
#   ====== 我的待办清单 ======
#   1. 查看待办
#   2. 新增待办
#   3. 标记完成
#   4. 删除待办
#   5. 退出
#
#   请选择操作：2
#   请输入待办内容：学习 Python 的函数
#
#   已添加：学习 Python 的函数
#
#   你当天要完成以下功能。
#
#   ## 1. 菜单循环
#
#   程序启动后反复显示菜单，直到用户输入 5：
#
#   1. 查看待办
#   2. 新增待办
#   3. 标记完成
#   4. 删除待办
#   5. 退出
#
#   输入无效，例如 9、abc、空内容时，提示错误并回到菜单，程序不能崩溃。
#
#   对应知识：while True、input()、if / elif / else、break。
#
#   ## 2. 新增待办
#
#   用户输入一段待办内容，程序将其加入列表。
#
#   要求：
#
#   - 去除前后空格：text.strip()
#   - 不允许空待办
#   - 新增后默认 done: false
#   - 保存到 todos.json
#
#   数据应长这样：
#
#   [
#     {
#       "title": "学习 Python 的函数",
#       "done": false
#     },
#     {
#       "title": "完成命令行待办项目",
#       "done": true
#     }
#   ]
#
#   对应知识：dict、list.append()、函数、JSON 写文件。
#
#   ## 3. 查看待办
#
#   显示所有事项和完成状态，例如：
#
#   ====== 待办清单 ======
#   1. [ ] 学习 Python 的函数
#   2. [x] 完成命令行待办项目
#
#   要求：
#
#   - 没有任何待办时显示“暂无待办”
#   - 序号从 1 开始显示，方便用户后续操作
#   - [ ] 表示未完成，[x] 表示已完成
#
#   对应知识：enumerate(todos, start=1)、循环、条件表达式。
#
#   ## 4. 标记完成
#
#   用户输入待办编号，例如输入 1，程序把第一项的 done 设为 True。
#
#   要求：
#
#   - 用户输入的编号应转换为整数
#   - 编号不存在时提示错误，例如“请输入 1 到 3 之间的编号”
#   - 已完成的事项再次标记时，应提示“该事项已经完成”
#   - 操作后立刻保存到 todos.json
#
#   对应知识：列表索引从 0 开始，所以用户输入的编号要减 1：
#
#   index = int(input("请输入待办编号：")) - 1
#   todos[index]["done"] = True
#
#   这一步要用 try/except ValueError 防止用户输入 hello 导致报错。
#
#   ## 5. 删除待办
#
#   用户输入待办编号，删除对应事项。
#
#   要求：
#
#   - 删除前显示要删除的内容，并要求确认：
#
#   确定删除“学习 Python 的函数”吗？(y/n)
#
#   - 只有输入 y 才真正删除
#   - 编号非法时不能删除任何数据
#   - 删除后自动保存
#
#   对应知识：list.pop(index)、字符串处理、函数、JSON 写文件。
#
#   ## 6. 程序启动时读取历史数据
#
#   下次运行时，之前新增的待办不能消失。
#
#   要求：
#
#   - 如果 todos.json 存在，读取它
#   - 如果文件不存在，使用空列表 []
#   - 如果 JSON 文件意外损坏，提示错误，但程序仍能启动；不要直接覆盖原文件
#
#   对应知识：Path.exists()、json.load()、try/except。
#
#   ## 7. 退出时安全保存
#
#   用户选择 5 后：
#
#   待办已保存，再见！
#
#   正常退出。为了简单起见，你可以每次新增、完成、删除后就保存；退出时再保存一次也没问题。
#
#   ## 建议的代码结构
#
#   不要把所有代码都写在最外层。至少拆成下面这些函数：
#
#   def load_todos():
#       pass
#
#   def save_todos(todos):
#       pass
#
#   def show_todos(todos):
#       pass
#
#   def add_todo(todos):
#       pass
#
#   def complete_todo(todos):
#       pass
#
#   def delete_todo(todos):
#       pass
#
#   def main():
#       pass
#
#   if __name__ == "__main__":
#       main()
#
#   这和 Java 的 main 方法类似：main() 负责程序流程；其他函数各自只处理一个明确的功能。
#
#   完成上述功能后，如果还有时间，再加两个选做功能：
#
#   - 编辑待办内容
#   - 只显示“未完成”事项