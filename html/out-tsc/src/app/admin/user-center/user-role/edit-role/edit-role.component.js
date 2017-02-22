var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ViewChild, Output, EventEmitter } from '@angular/core';
import { NgForm } from "@angular/forms";
import { Http } from "@angular/http";
import { GlobalService } from "../../../../core/global.service";
import { Role } from "../role";
export var EditRoleComponent = (function () {
    function EditRoleComponent(http, gs) {
        this.http = http;
        this.gs = gs;
        this.role = new Role();
        this.completed = new EventEmitter();
        this.formErrors = {
            'name': '',
            'remark': ''
        };
        this.validationMessages = {
            'name': {
                'required': '角色名为必填字段。',
                'minlength': '角色名不得少于5个字符。',
                'maxlength': '角色名不得超30个字符。'
            },
            'remark': {
                'maxlength': '备注长度不得超255个字符。'
            }
        };
    }
    EditRoleComponent.prototype.ngOnInit = function () {
    };
    EditRoleComponent.prototype.show = function (role) {
        this.role = role;
        $('#edit_role_modal').modal('show');
    };
    EditRoleComponent.prototype.hide = function () {
        $('#edit_role_modal').modal('hide');
    };
    EditRoleComponent.prototype.ngAfterViewChecked = function () {
        this.FormChanged();
    };
    EditRoleComponent.prototype.FormChanged = function () {
        var _this = this;
        if (this.currentForm === this.updateRoleForm) {
            return;
        }
        this.updateRoleForm = this.currentForm;
        if (this.updateRoleForm) {
            this.updateRoleForm.valueChanges.subscribe(function (data) {
                if (!_this.updateRoleForm) {
                    return;
                }
                var form = _this.updateRoleForm.form;
                _this.onValueChanged(form, data);
            });
        }
    };
    EditRoleComponent.prototype.onValueChanged = function (form, data) {
        for (var field in this.formErrors) {
            this.formErrors[field] = '';
            var control = form.get(field);
            if (control && control.dirty && !control.valid) {
                var messages = this.validationMessages[field];
                for (var key in control.errors) {
                    this.formErrors[field] += messages[key] + ' ';
                }
            }
        }
    };
    EditRoleComponent.prototype.onSubmit = function () {
        var _this = this;
        var payload = {};
        if (this.role.name.length > 0) {
            payload['name'] = this.role.name;
        }
        payload['remark'] = this.role.remark;
        var url = this.gs.updateRoleURL + this.role.id.toString();
        var sc = this.http.patch(url, payload, this.gs.jsonHeadersWithCredentials).subscribe(function (req) {
            sc.unsubscribe();
            _this.completed.emit();
            _this.gs.showingTopFlashMessageSuccess();
        }, function (err) {
            console.log(err);
            _this.gs.showingTopFlashMessageError();
        }, function () {
        });
        this.currentForm.reset();
        this.hide();
    };
    __decorate([
        ViewChild("updateRoleForm"), 
        __metadata('design:type', NgForm)
    ], EditRoleComponent.prototype, "currentForm", void 0);
    __decorate([
        Output(), 
        __metadata('design:type', Object)
    ], EditRoleComponent.prototype, "completed", void 0);
    EditRoleComponent = __decorate([
        Component({
            selector: 'app-edit-role',
            templateUrl: './edit-role.component.html',
            styleUrls: ['./edit-role.component.css']
        }), 
        __metadata('design:paramtypes', [Http, GlobalService])
    ], EditRoleComponent);
    return EditRoleComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/user-center/user-role/edit-role/edit-role.component.js.map