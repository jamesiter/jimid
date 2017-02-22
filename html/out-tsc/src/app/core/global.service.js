var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Http } from "@angular/http";
import { Router } from "@angular/router";
export var GlobalService = (function () {
    function GlobalService(_http, router) {
        this._http = _http;
        this.router = router;
        this.current_user = {};
        this.jsonHeaders = new Headers({ 'Content-Type': 'application/json' });
        this.jsonHeadersWithCredentials = new RequestOptions({ headers: this.jsonHeaders, withCredentials: true });
        // public http = 'http://';
        // public https = 'https://';
        // public domain  = 'dev.iit.im';
        // public hostName = 'jimauth';
        // public fqdn = this.hostName + '.' + this.domain;
        // public httpURL= this.http + this.fqdn;
        // public httpsURL= this.https + this.fqdn;
        // public baseURL = this.httpURL;
        this.baseURL = document.location.protocol + '//' + document.location.hostname + ':' + document.location.port;
        this.APIBaseURL = this.baseURL + '/api';
        this.authURL = this.APIBaseURL + '/user/_auth';
        this.signUpURL = this.APIBaseURL + '/user/_sign_up';
        this.signInURL = this.APIBaseURL + '/user/_sign_in';
        this.signInByMobilePhoneURL = this.APIBaseURL + '/user/_sign_in_by_mobile_phone';
        this.signInByEMailURL = this.APIBaseURL + '/user/_sign_in_by_email';
        this.signOutURL = this.APIBaseURL + '/user/_sign_out';
        // 获取用户所拥有的应用列表
        this.getSelfAppListURL = this.APIBaseURL + '/user/_app_list';
        // 获取用户自己的用户信息
        this.getSelfInfoURL = this.APIBaseURL + '/user';
        this.searchUsersURL = this.APIBaseURL + '/users_mgmt/_search';
        // 更新单个用户信息
        this.updateUserURL = this.APIBaseURL + '/user_mgmt/';
        // 批量更新用户信息
        this.updateUsersURL = this.APIBaseURL + '/users_mgmt';
        // 激活指定用户
        this.enableUserURL = this.APIBaseURL + '/user_mgmt/_enable/';
        // 禁用指定用户
        this.disableUserURL = this.APIBaseURL + '/user_mgmt/_disable/';
        // 获取单个用户信息
        this.getUserURL = this.APIBaseURL + '/user_mgmt/';
        // 通过过滤获取相关用户信息
        this.getUsersURL = this.APIBaseURL + '/users_mgmt';
        // 删除单个用户信息
        this.deleteUserURL = this.APIBaseURL + '/user_mgmt/';
        // 更新指定用户密码
        this.resetPasswordURL = this.APIBaseURL + '/user_mgmt/_change_password/';
        // 获取App
        this.searchAppsURL = this.APIBaseURL + '/apps/_search';
        // 创建App
        this.createAppURL = this.APIBaseURL + '/app';
        // 更新App
        this.updateAppURL = this.APIBaseURL + '/app/';
        // 删除App
        this.deleteAppURL = this.APIBaseURL + '/app/';
        this.searchOpenidsURL = this.APIBaseURL + '/openids_mgmt/_search';
        this.updateOpenidURL = this.APIBaseURL + '/openid_mgmt/';
        this.deleteOpenidURL = this.APIBaseURL + '/openid_mgmt/';
        // 通过角色ID获取应用
        this.getAppByRoleIDURL = this.APIBaseURL + '/roles/_get_app_by_role_id/';
        // 获取角色及用户和应用的映射
        this.getUserRoleAppMappingURL = this.APIBaseURL + '/roles/_get_user_role_app_mapping';
        // 创建角色
        this.createRoleURL = this.APIBaseURL + '/role';
        // 更新角色
        this.updateRoleURL = this.APIBaseURL + '/role/';
        // 删除角色
        this.deleteRoleURL = this.APIBaseURL + '/role/';
        // 添加用户成员到角色
        this.addMemberToRoleURL = this.APIBaseURL + '/role/_add_user_to_role/';
        // 从角色删除用户成员
        this.deleteMemberFromRoleURL = this.APIBaseURL + '/role/_delete_user_from_role/';
        // 添加应用到角色
        this.addAppToRoleURL = this.APIBaseURL + '/role/_add_app_to_role/';
        // 从角色删除应用
        this.deleteAppFromRoleURL = this.APIBaseURL + '/role/_delete_app_from_role/';
        // 从不属于任何角色的用户中模糊查找
        this.searchRoleFreeUsersURL = this.APIBaseURL + '/roles/_search_with_free_users';
        // 获取不属于该角色的其它应用
        this.getRoleOtherAppsURL = this.APIBaseURL + '/apps';
        this.topFlashMessage = '';
        this.topFlashMessageType = 'success';
        this.topFlashSuccessMessage = '操作已经成功完成';
        this.topFlashLoadingMessage = '正在努力加载中';
        this.topFlashErrorMessage = '操作失败';
        this.timer = 10;
        this.topFlashMessageDuration = 3;
        this.timerRun();
        console.log(this.baseURL);
    }
    GlobalService.prototype.timerRun = function () {
        var _this = this;
        setInterval(function () {
            if (_this.timer > 0) {
                _this.timer--;
            }
        }, 1000);
    };
    GlobalService.prototype.showingTopFlashMessage = function (message, type, time) {
        this.topFlashMessage = message;
        this.topFlashMessageType = type;
        this.timer = time;
    };
    GlobalService.prototype.showingTopFlashMessageSuccess = function (message) {
        if (message === void 0) { message = this.topFlashSuccessMessage; }
        this.showingTopFlashMessage(message, 'success', this.topFlashMessageDuration);
    };
    GlobalService.prototype.showingTopFlashMessageLoading = function (message) {
        if (message === void 0) { message = this.topFlashSuccessMessage; }
        this.showingTopFlashMessage(message, 'loading', this.topFlashMessageDuration);
    };
    GlobalService.prototype.showingTopFlashMessageError = function (message) {
        if (message === void 0) { message = this.topFlashErrorMessage; }
        this.showingTopFlashMessage(message, 'error', this.topFlashMessageDuration);
    };
    GlobalService.prototype.getSelfInfo = function () {
        var _this = this;
        var sc = this._http.get(this.getSelfInfoURL, this.jsonHeadersWithCredentials).subscribe(function (req) {
            if (req.status == 200) {
                console.log('Get self info succeed!');
                _this.current_user = req.json().data || {};
                _this.roleObserver.next(_this.current_user.manager);
            }
            sc.unsubscribe();
        }, function (err) {
            console.log('Get self info failed!');
            console.log(err.toString());
        }, function () {
            console.log('Get self info complete!');
        });
    };
    GlobalService.prototype.navigate = function (url, queryParams) {
        if (queryParams === void 0) { queryParams = {}; }
        this.router.navigate([url], { queryParams: queryParams });
    };
    GlobalService = __decorate([
        Injectable(), 
        __metadata('design:paramtypes', [Http, Router])
    ], GlobalService);
    return GlobalService;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/core/global.service.js.map