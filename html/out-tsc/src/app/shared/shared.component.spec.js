import { async, TestBed } from '@angular/core/testing';
import { SharedComponent } from './shared.component';
describe('SharedComponent', function () {
    var component;
    var fixture;
    beforeEach(async(function () {
        TestBed.configureTestingModule({
            declarations: [SharedComponent]
        })
            .compileComponents();
    }));
    beforeEach(function () {
        fixture = TestBed.createComponent(SharedComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', function () {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=/Users/James/PycharmProjects/jimid-web/src/src/app/shared/shared.component.spec.js.map