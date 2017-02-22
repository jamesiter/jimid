import { async, TestBed } from '@angular/core/testing';
import { TopNavComponent } from './top-nav.component';
describe('TopNavComponent', function () {
    var component;
    var fixture;
    beforeEach(async(function () {
        TestBed.configureTestingModule({
            declarations: [TopNavComponent]
        })
            .compileComponents();
    }));
    beforeEach(function () {
        fixture = TestBed.createComponent(TopNavComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', function () {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/admin/top-nav/top-nav.component.spec.js.map