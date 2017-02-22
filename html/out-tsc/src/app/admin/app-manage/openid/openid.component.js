var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component } from '@angular/core';
import { Http, URLSearchParams } from "@angular/http";
import { GlobalService } from "../../../core/global.service";
import { ActivatedRoute } from "@angular/router";
import { Subject } from "rxjs";
export var OpenidComponent = (function () {
    function OpenidComponent(http, gs, activatedRoute) {
        var _this = this;
        this.http = http;
        this.gs = gs;
        this.activatedRoute = activatedRoute;
        this.openids = [];
        this.page = 1;
        this.pages = [];
        this.pageSize = 10;
        this.pageTotal = 0;
        this.pageWidth = 10;
        this.balanceOfPower = Math.floor(this.pageWidth / 2) + 1;
        this.lastPagination = Math.ceil(this.pageTotal / this.pageSize);
        this.startPagination = 1;
        this.endPagination = this.lastPagination;
        this.keyword = '';
        this.searchContentStream = new Subject();
        this.subscription = this.activatedRoute.queryParams.subscribe(function (queryParams) {
            _this.page = +queryParams['page'] || _this.page;
            _this.pageSize = +queryParams['page_size'] || _this.pageSize;
            _this.keyword = queryParams['keyword'] || _this.keyword;
            _this.getOpenids();
        }, function (err) {
            console.log(err);
        }, function () {
            console.log('complete!');
        });
        this.subscriptionBySearch = this.searchContentStream
            .debounceTime(300)
            .distinctUntilChanged()
            .do(function (keyword) {
            _this.keyword = keyword;
        }).subscribe(function (next) {
            var params = {};
            params['page'] = _this.page.toString();
            params['page_size'] = _this.pageSize.toString();
            if (_this.keyword.length > 0) {
                params['keyword'] = _this.keyword.toString();
            }
            _this.gs.navigate('/admin/app-manage/openid', params);
        }, function (err) {
            console.log(err);
        }, function () {
        });
    }
    OpenidComponent.prototype.searchContent = function (keyword) {
        this.page = 1;
        this.searchContentStream.next(keyword);
    };
    OpenidComponent.prototype.ngOnInit = function () {
    };
    OpenidComponent.prototype.ngAfterViewInit = function () {
    };
    OpenidComponent.prototype.ngOnDestroy = function () {
        this.subscription.unsubscribe();
        this.subscriptionBySearch.unsubscribe();
    };
    OpenidComponent.prototype.getOpenids = function () {
        var _this = this;
        var params = new URLSearchParams();
        params.set('page', this.page.toString());
        params.set('page_size', this.pageSize.toString());
        if (this.keyword.length > 0) {
            params.set('keyword', this.keyword.toString());
        }
        var sc = this.http.get(this.gs.searchOpenidsURL, { withCredentials: true, search: params }).subscribe(function (req) {
            if (req.status == 200) {
                var data = req.json();
                _this.pageTotal = data.paging.total;
                _this.openids = data.data;
                _this.refreshPageState();
                sc.unsubscribe();
            }
        }, function (err) {
            console.log(err);
        }, function () {
        });
    };
    OpenidComponent.prototype.refresh = function () {
        var params = {};
        params['page'] = this.page.toString();
        params['page_size'] = this.pageSize.toString();
        if (this.keyword.length > 0) {
            params['keyword'] = this.keyword.toString();
        }
        this.gs.navigate('/admin/app-manage/openid', params);
    };
    ;
    OpenidComponent.prototype.changePage = function (thePage) {
        this.page = thePage;
        this.refresh();
    };
    OpenidComponent.prototype.changePageSize = function (thePageSize) {
        this.pageSize = thePageSize;
        this.page = 1;
        this.refresh();
    };
    OpenidComponent.prototype.refreshPageState = function () {
        this.lastPagination = Math.ceil(this.pageTotal / this.pageSize);
        this.startPagination = 1;
        this.endPagination = this.lastPagination;
        if (this.page > this.balanceOfPower) {
            this.startPagination = this.page - Math.floor(this.pageWidth / 2);
        }
        if (this.page < this.lastPagination - (this.pageWidth - this.balanceOfPower)) {
            if (this.page < this.balanceOfPower) {
                if (this.lastPagination > this.pageWidth) {
                    this.endPagination = this.pageWidth;
                }
            }
            else {
                this.endPagination = this.page + (this.pageWidth - this.balanceOfPower);
            }
        }
        else {
            if (this.lastPagination > this.pageWidth && (this.endPagination - this.startPagination) < this.pageWidth) {
                this.startPagination = this.lastPagination - (this.pageWidth - 1);
            }
        }
        while (this.pages.length) {
            this.pages.pop();
        }
        for (var _i = this.startPagination; _i <= this.endPagination; _i++) {
            this.pages.push(_i);
        }
    };
    OpenidComponent = __decorate([
        Component({
            selector: 'app-openid',
            templateUrl: './openid.component.html',
            styleUrls: ['./openid.component.css']
        }), 
        __metadata('design:paramtypes', [Http, GlobalService, ActivatedRoute])
    ], OpenidComponent);
    return OpenidComponent;
}());
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/app-manage/openid/openid.component.js.map