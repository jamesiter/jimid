/**
 * @fileoverview This file is generated by the Angular 2 template compiler.
 * Do not edit.
 * @suppress {suspiciousCode,uselessCode,missingProperties}
 */
/* tslint:disable */
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
import * as import0 from './user.component';
import * as import1 from '@angular/core/src/linker/view';
import * as import3 from '@angular/core/src/linker/view_utils';
import * as import4 from '@angular/core/src/metadata/view';
import * as import5 from '@angular/core/src/linker/view_type';
import * as import6 from '@angular/core/src/change_detection/change_detection';
import * as import7 from '@angular/core/src/linker/component_factory';
import * as import8 from '@angular/http/src/http';
import * as import9 from '../core/global.service';
import * as import10 from '../../assets/src/scss/custom.css';
import * as import11 from './user.component.css';
import * as import12 from './user-top-nav/user-top-nav.component';
import * as import13 from './user-top-nav/user-top-nav.component.ngfactory';
import * as import14 from '@angular/core/src/linker/view_container';
import * as import15 from '../../../node_modules/@angular/router/src/directives/router_outlet.ngfactory';
import * as import16 from './user-footer/user-footer.component';
import * as import17 from './user-footer/user-footer.component.ngfactory';
import * as import18 from '../core/auth.service';
import * as import19 from '@angular/router/src/router_outlet_map';
import * as import20 from '@angular/core/src/linker/component_factory_resolver';
import * as import21 from '@angular/router/src/directives/router_outlet';
export var Wrapper_UserComponent = (function () {
    function Wrapper_UserComponent(p0, p1) {
        this._changed = false;
        this.context = new import0.UserComponent(p0, p1);
    }
    Wrapper_UserComponent.prototype.ngOnDetach = function (view, componentView, el) {
    };
    Wrapper_UserComponent.prototype.ngOnDestroy = function () {
    };
    Wrapper_UserComponent.prototype.ngDoCheck = function (view, el, throwOnChange) {
        var changed = this._changed;
        this._changed = false;
        if (!throwOnChange) {
            if ((view.numberOfChecks === 0)) {
                this.context.ngOnInit();
            }
        }
        return changed;
    };
    Wrapper_UserComponent.prototype.checkHost = function (view, componentView, el, throwOnChange) {
    };
    Wrapper_UserComponent.prototype.handleEvent = function (eventName, $event) {
        var result = true;
        return result;
    };
    Wrapper_UserComponent.prototype.subscribe = function (view, _eventHandler) {
        this._eventHandler = _eventHandler;
    };
    return Wrapper_UserComponent;
}());
var renderType_UserComponent_Host = import3.createRenderComponentType('', 0, import4.ViewEncapsulation.None, [], {});
var View_UserComponent_Host0 = (function (_super) {
    __extends(View_UserComponent_Host0, _super);
    function View_UserComponent_Host0(viewUtils, parentView, parentIndex, parentElement) {
        _super.call(this, View_UserComponent_Host0, renderType_UserComponent_Host, import5.ViewType.HOST, viewUtils, parentView, parentIndex, parentElement, import6.ChangeDetectorStatus.CheckAlways);
    }
    View_UserComponent_Host0.prototype.createInternal = function (rootSelector) {
        this._el_0 = import3.selectOrCreateRenderHostElement(this.renderer, 'app-user', import3.EMPTY_INLINE_ARRAY, rootSelector, null);
        this.compView_0 = new View_UserComponent0(this.viewUtils, this, 0, this._el_0);
        this._UserComponent_0_3 = new Wrapper_UserComponent(this.injectorGet(import8.Http, this.parentIndex), this.injectorGet(import9.GlobalService, this.parentIndex));
        this.compView_0.create(this._UserComponent_0_3.context);
        this.init(this._el_0, (this.renderer.directRenderer ? null : [this._el_0]), null);
        return new import7.ComponentRef_(0, this, this._el_0, this._UserComponent_0_3.context);
    };
    View_UserComponent_Host0.prototype.injectorGetInternal = function (token, requestNodeIndex, notFoundResult) {
        if (((token === import0.UserComponent) && (0 === requestNodeIndex))) {
            return this._UserComponent_0_3.context;
        }
        return notFoundResult;
    };
    View_UserComponent_Host0.prototype.detectChangesInternal = function (throwOnChange) {
        this._UserComponent_0_3.ngDoCheck(this, this._el_0, throwOnChange);
        this.compView_0.detectChanges(throwOnChange);
    };
    View_UserComponent_Host0.prototype.destroyInternal = function () {
        this.compView_0.destroy();
    };
    View_UserComponent_Host0.prototype.visitRootNodesInternal = function (cb, ctx) {
        cb(this._el_0, ctx);
    };
    return View_UserComponent_Host0;
}(import1.AppView));
export var UserComponentNgFactory = new import7.ComponentFactory('app-user', View_UserComponent_Host0, import0.UserComponent);
var styles_UserComponent = [
    import10.styles,
    import11.styles
];
var renderType_UserComponent = import3.createRenderComponentType('', 0, import4.ViewEncapsulation.None, styles_UserComponent, {});
export var View_UserComponent0 = (function (_super) {
    __extends(View_UserComponent0, _super);
    function View_UserComponent0(viewUtils, parentView, parentIndex, parentElement) {
        _super.call(this, View_UserComponent0, renderType_UserComponent, import5.ViewType.COMPONENT, viewUtils, parentView, parentIndex, parentElement, import6.ChangeDetectorStatus.CheckAlways);
    }
    View_UserComponent0.prototype.createInternal = function (rootSelector) {
        var parentRenderNode = this.renderer.createViewRoot(this.parentElement);
        this._el_0 = import3.createRenderElement(this.renderer, parentRenderNode, 'body', new import3.InlineArray2(2, 'class', 'nav-md'), null);
        this._text_1 = this.renderer.createText(this._el_0, '\n', null);
        this._el_2 = import3.createRenderElement(this.renderer, this._el_0, 'div', new import3.InlineArray2(2, 'class', 'container body'), null);
        this._text_3 = this.renderer.createText(this._el_2, '\n  ', null);
        this._el_4 = import3.createRenderElement(this.renderer, this._el_2, 'div', new import3.InlineArray2(2, 'class', 'main_container'), null);
        this._text_5 = this.renderer.createText(this._el_4, '\n    ', null);
        this._el_6 = import3.createRenderElement(this.renderer, this._el_4, 'app-user-top-nav', import3.EMPTY_INLINE_ARRAY, null);
        this.compView_6 = new import13.View_UserTopNavComponent0(this.viewUtils, this, 6, this._el_6);
        this._UserTopNavComponent_6_3 = new import13.Wrapper_UserTopNavComponent(this.parentView.injectorGet(import18.AuthService, this.parentIndex), this.parentView.injectorGet(import9.GlobalService, this.parentIndex));
        this.compView_6.create(this._UserTopNavComponent_6_3.context);
        this._text_7 = this.renderer.createText(this._el_4, '\n    ', null);
        this._text_8 = this.renderer.createText(this._el_4, '\n    ', null);
        this._el_9 = import3.createRenderElement(this.renderer, this._el_4, 'div', new import3.InlineArray2(2, 'role', 'main'), null);
        this._text_10 = this.renderer.createText(this._el_9, '\n      ', null);
        this._el_11 = import3.createRenderElement(this.renderer, this._el_9, 'router-outlet', import3.EMPTY_INLINE_ARRAY, null);
        this._vc_11 = new import14.ViewContainer(11, 9, this, this._el_11);
        this._RouterOutlet_11_5 = new import15.Wrapper_RouterOutlet(this.parentView.injectorGet(import19.RouterOutletMap, this.parentIndex), this._vc_11.vcRef, this.parentView.injectorGet(import20.ComponentFactoryResolver, this.parentIndex), null);
        this._text_12 = this.renderer.createText(this._el_9, '\n    ', null);
        this._text_13 = this.renderer.createText(this._el_4, '\n    ', null);
        this._text_14 = this.renderer.createText(this._el_4, '\n    ', null);
        this._el_15 = import3.createRenderElement(this.renderer, this._el_4, 'app-user-footer', import3.EMPTY_INLINE_ARRAY, null);
        this.compView_15 = new import17.View_UserFooterComponent0(this.viewUtils, this, 15, this._el_15);
        this._UserFooterComponent_15_3 = new import17.Wrapper_UserFooterComponent();
        this.compView_15.create(this._UserFooterComponent_15_3.context);
        this._text_16 = this.renderer.createText(this._el_4, '\n  ', null);
        this._text_17 = this.renderer.createText(this._el_2, '\n', null);
        this._text_18 = this.renderer.createText(this._el_0, '\n', null);
        this._text_19 = this.renderer.createText(parentRenderNode, '\n', null);
        this.init(null, (this.renderer.directRenderer ? null : [
            this._el_0,
            this._text_1,
            this._el_2,
            this._text_3,
            this._el_4,
            this._text_5,
            this._el_6,
            this._text_7,
            this._text_8,
            this._el_9,
            this._text_10,
            this._el_11,
            this._text_12,
            this._text_13,
            this._text_14,
            this._el_15,
            this._text_16,
            this._text_17,
            this._text_18,
            this._text_19
        ]), null);
        return null;
    };
    View_UserComponent0.prototype.injectorGetInternal = function (token, requestNodeIndex, notFoundResult) {
        if (((token === import12.UserTopNavComponent) && (6 === requestNodeIndex))) {
            return this._UserTopNavComponent_6_3.context;
        }
        if (((token === import21.RouterOutlet) && (11 === requestNodeIndex))) {
            return this._RouterOutlet_11_5.context;
        }
        if (((token === import16.UserFooterComponent) && (15 === requestNodeIndex))) {
            return this._UserFooterComponent_15_3.context;
        }
        return notFoundResult;
    };
    View_UserComponent0.prototype.detectChangesInternal = function (throwOnChange) {
        var currVal_6_0_0 = this.context.gs.current_user.login_name;
        this._UserTopNavComponent_6_3.check_login_name(currVal_6_0_0, throwOnChange, false);
        this._UserTopNavComponent_6_3.ngDoCheck(this, this._el_6, throwOnChange);
        this._RouterOutlet_11_5.ngDoCheck(this, this._el_11, throwOnChange);
        this._UserFooterComponent_15_3.ngDoCheck(this, this._el_15, throwOnChange);
        this._vc_11.detectChangesInNestedViews(throwOnChange);
        this.compView_6.detectChanges(throwOnChange);
        this.compView_15.detectChanges(throwOnChange);
    };
    View_UserComponent0.prototype.destroyInternal = function () {
        this._vc_11.destroyNestedViews();
        this.compView_6.destroy();
        this.compView_15.destroy();
        this._RouterOutlet_11_5.ngOnDestroy();
    };
    return View_UserComponent0;
}(import1.AppView));
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/user/user.component.ngfactory.js.map