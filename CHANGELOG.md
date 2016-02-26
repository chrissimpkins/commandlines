### v0.4.0

- added support for default option-argument assignments
- new `Command.defaults` instance attribute (Python dictionary)
- new `Command.set_defaults()` method
- new `Command.contains_defaults()` method
- new `Command.get_default()` method
- updated string returned by `Command.obj_string()` method with parsed default option-argument definitions

### v0.3.3

- added verbose option testing method to Command class
- added quiet option testing method to Command class

### v0.3.2

- Command object string parsing performance improvements
- Refactored Mops instantiation method argument parsing loops (performance optimization)
- Refactored Definitions instantiation method argument parsing loops (performance optimization)
- Refactored MultiDefinitions instantiation method argument parsing loops (performance optimization)
- Refactored Switches instantiation method argument parsing loops (performance optimization)

### v0.3.1

- Added Command `obj_string()` method to support inspection of parsed command arguments in Command object attributes

### v0.3.0

- initial public release