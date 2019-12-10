import requests

import api

class ApiEmployee:
    #初始化
    def __init__(self):
        #添加员工
        self.url_add = api.BASE_URL + "/api/sys/user"
        #员工 {}为占位符 引用.format(id)
        self.url_employee = api.BASE_URL+"/api/sys/user/{}"

     #添加员工
    def api_post_employee(self,username,mobile,workNumber):
        #定义json数据
        data = {"username":username,
                "mobile":mobile,
                "workNumber":workNumber}
        #调用post方法   必须return
        return requests.post(url=self.url_add,json=data,headers=api.headers)

    #修改员工
    def api_put_employee(self,username):
        data = {"username":username}
        return requests.put(url=self.url_employee.format(api.user_id),json=data,headers=api.headers)

    #查询员工
    def api_get_employee(self):
        return requests.get(url=self.url_employee.format(api.user_id),headers=api.headers)

    #删除员工
    def api_delete_employee(self):
        return requests.delete(url=self.url_employee.format(api.user_id), headers=api.headers)