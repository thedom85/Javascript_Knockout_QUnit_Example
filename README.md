# Javascript_Knockout_QUnit_Example
 
Example simplified view model:

```javascript
function MarkersViewModel() {
    var self = this;   
    self.name = ko.observable("chad");
    self.computedName = ko.computed(function() {
        return self.name();
	});
}
```
Example of unit test 

```javascript
test(" Test view_model.name ", function () {
    var view_model = new MarkersViewModel();
    view_model.name("joe");
    equal(view_model.computedName(), "joe");
 
});

```
