#!/usr/bin/env python
# -*- coding: utf-8 -*-


from models.utils import add_rule
from views import user, mgmt


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


# 普通用户接口
# 注册
add_rule(user.blueprint, '/_sign_up', view_func='user.r_sign_up', methods=['POST'])
# 通过手机号码注册
add_rule(user.blueprint, '/_sign_up_by_mobile_phone', view_func='user.r_sign_up_by_mobile_phone', methods=['POST'])
# 通过email注册
add_rule(user.blueprint, '/_sign_up_by_email', view_func='user.r_sign_up_by_email', methods=['POST'])
# 登录
add_rule(user.blueprint, '/_sign_in', view_func='user.r_sign_in', methods=['POST'])
add_rule(user.blueprint, '/_sign_in_by_mobile_phone', view_func='user.r_sign_in_by_mobile_phone', methods=['POST'])
add_rule(user.blueprint, '/_sign_in_by_email', view_func='user.r_sign_in_by_email', methods=['POST'])
# 登出
add_rule(user.blueprint, '/_sign_out', view_func='user.r_sign_out', methods=['GET'])
# 验证
add_rule(user.blueprint, '/_auth', view_func='user.r_auth', methods=['GET'])
# 获取用户信息
add_rule(user.blueprint, '', view_func='user.r_get', methods=['GET'])
# 更改用户密码
add_rule(user.blueprint, '/_change_password', view_func='user.r_change_password', methods=['PATCH'])

# 管理接口
# 通过用户名获取用户信息
add_rule(mgmt.blueprint, '/_by_login_name/<login_name>', view_func='mgmt.r_get_by_login_name', methods=['GET'])
# 删除用户(用户不可以删除自身,说白了只能超级用户删除普通用户,且超级用户不能删除自己)
add_rule(mgmt.blueprint, '/<_id>', view_func='mgmt.r_delete', methods=['DELETE'])
# 禁用用户(用户不可以禁用自身,只能超级用户禁用普通用户,且超级用户不能禁用自己)
add_rule(mgmt.blueprint, '/_disable/<_id>', view_func='mgmt.r_disable', methods=['PATCH'])
# 解禁用户(用户不可以解禁自身,只能超级用户解禁普通用户,且超级用户不能解禁自己)
add_rule(mgmt.blueprint, '/_enable/<_id>', view_func='mgmt.r_enable', methods=['PATCH'])
# 管理员更新用户信息
add_rule(mgmt.blueprint, '', view_func='mgmt.r_update', methods=['PATCH'])

# 管理员批量操作用户信息
add_rule(mgmt.blueprints, '', view_func='mgmt.r_get_by_filter', methods=['GET'])
add_rule(mgmt.blueprints, '', view_func='mgmt.r_update_by_uid_s', methods=['PATCH'])
add_rule(mgmt.blueprints, '', view_func='mgmt.r_delete_by_uid_s', methods=['DELETE'])
add_rule(mgmt.blueprints, '/_search', view_func='mgmt.r_content_search', methods=['GET'])

