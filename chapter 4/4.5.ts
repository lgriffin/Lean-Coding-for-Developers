// Hard to delete: implicitly depends on global state
function process() {
  const config = globalConfig.processingRules; // Where did this come from?
}

// Easy to delete: explicitly declared
function process(config: ProcessingRules) {
  // Clear what this needs
}
