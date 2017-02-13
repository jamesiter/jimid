#!/usr/bin/env python
# -*- coding: utf-8 -*-


from models.utils import add_rule
from views import openid_admin, role
from views import user, user_mgmt, openid, app


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
# 获取用户应用列表
add_rule(user.blueprint, '/_app_list', view_func='user.r_app_list', methods=['GET'])

# 管理接口
# 通过uid获取用户信息
add_rule(user_mgmt.blueprint, '/<_id>', view_func='user_mgmt.r_get', methods=['GET'])
# 通过用户名获取用户信息
add_rule(user_mgmt.blueprint, '/_by_login_name/<login_name>', view_func='user_mgmt.r_get_by_login_name',
         methods=['GET'])
# 删除用户(用户不可以删除自身,说白了只能超级用户删除普通用户,且超级用户不能删除自己)
add_rule(user_mgmt.blueprint, '/<_id>', view_func='user_mgmt.r_delete', methods=['DELETE'])
# 禁用用户(用户不可以禁用自身,只能超级用户禁用普通用户,且超级用户不能禁用自己)
add_rule(user_mgmt.blueprint, '/_disable/<_id>', view_func='user_mgmt.r_disable', methods=['PATCH'])
# 解禁用户(用户不可以解禁自身,只能超级用户解禁普通用户,且超级用户不能解禁自己)
add_rule(user_mgmt.blueprint, '/_enable/<_id>', view_func='user_mgmt.r_enable', methods=['PATCH'])
# 管理员更新用户信息
add_rule(user_mgmt.blueprint, '/<_id>', view_func='user_mgmt.r_update', methods=['PATCH'])
# 管理员更新用户密码
add_rule(user_mgmt.blueprint, '/_change_password/<_id>', view_func='user_mgmt.r_change_password', methods=['PATCH'])

# 管理员批量操作用户信息
add_rule(user_mgmt.blueprints, '', view_func='user_mgmt.r_get_by_filter', methods=['GET'])
add_rule(user_mgmt.blueprints, '', view_func='user_mgmt.r_update_by_uid_s', methods=['PATCH'])
add_rule(user_mgmt.blueprints, '', view_func='user_mgmt.r_delete_by_uid_s', methods=['DELETE'])
add_rule(user_mgmt.blueprints, '/_search', view_func='user_mgmt.r_content_search', methods=['GET'])

# openid注册、绑定、解绑接口
add_rule(openid.blueprint, '/_sign_up', view_func='openid.r_sign_up', methods=['GET'])
add_rule(openid.blueprint, '/_bind', view_func='openid.r_bind', methods=['GET'])
add_rule(openid.blueprint, '/_unbind', view_func='openid.r_unbind', methods=['GET'])
add_rule(openid.blueprint, '/_auth', view_func='openid.r_auth', methods=['GET'])

# app操作接口
add_rule(app.blueprint, '', view_func='app.r_create', methods=['POST'])
add_rule(app.blueprint, '', view_func='app.r_update', methods=['PATCH'])
add_rule(app.blueprint, '/<_id>', view_func='app.r_delete', methods=['DELETE'])
add_rule(app.blueprints, '', view_func='app.r_get_by_filter', methods=['GET'])
add_rule(app.blueprints, '/_search', view_func='app.r_content_search', methods=['GET'])

# openid管理接口
add_rule(openid_admin.blueprint, '', view_func='openid_admin.r_update', methods=['PATCH'])
add_rule(openid_admin.blueprint, '/<appid>/<uid>', view_func='openid_admin.r_delete', methods=['DELETE'])
add_rule(openid_admin.blueprints, '', view_func='openid_admin.r_get_by_filter', methods=['GET'])
add_rule(openid_admin.blueprints, '/_search', view_func='openid_admin.r_content_search', methods=['GET'])

# role管理接口
# 创建角色
add_rule(role.blueprint, '', view_func='role.r_create', methods=['POST'])
# 获取角色
add_rule(role.blueprints, '', view_func='role.r_get_by_filter', methods=['GET'])
# 依据角色id获取应用
add_rule(role.blueprints, '/_get_app_by_role_id/<role_id>', view_func='role.r_get_app_by_role_id', methods=['GET'])
# 获取角色本身，及其所关联的用户和应用
add_rule(role.blueprints, '/_get_user_role_app_mapping', view_func='role.r_get_user_role_app_mapping', methods=['GET'])
# 更新角色
add_rule(role.blueprint, '/<_id>', view_func='role.r_update', methods=['PATCH'])
# 删除角色
add_rule(role.blueprint, '/<_id>', view_func='role.r_delete', methods=['DELETE'])
# 给角色加入用户
add_rule(role.blueprint, '/_add_user_to_role/<role_id>/<uid>', view_func='role.r_add_user_to_role', methods=['POST'])
# 把用户从角色删除
add_rule(role.blueprint, '/_delete_user_from_role/<role_id>/<uid>', view_func='role.r_delete_user_from_role',
         methods=['DELETE'])
# 给角色加入应用
add_rule(role.blueprint, '/_add_app_to_role/<role_id>/<appid>', view_func='role.r_add_app_to_role', methods=['POST'])
# 把应用从角色删除
add_rule(role.blueprint, '/_delete_app_from_role/<role_id>/<appid>', view_func='role.r_delete_app_from_role',
         methods=['DELETE'])
# 模糊查找不属于任何角色的用户
add_rule(role.blueprints, '/_search_with_free_users', view_func='role.r_content_search_with_free_users', methods=['GET'])

