
//Example simplified view model:
function MarkersViewModel() {
    var self = this;   
    self.name = ko.observable("chad");
    self.computedName = ko.computed(function() {
        return self.name();
	});
}