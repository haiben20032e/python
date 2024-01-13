#modun là 1 tập tin python có đuôi là "py",trong đó chứa một tập tin các hàm. modun có thể coi như là một thư viện, bạn cần import vào tệp muốn dùng
def countword(str):
    return len(str.split())
#hàm xóa ký tự đặc biệt
def removespecialchar(str):
    result=""
    specials=["$","#","@","*","%","&","!"]
    for c in str:
        if c not in specials:
            result+=c
    return result
