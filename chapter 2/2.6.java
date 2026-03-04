// Simple, sufficient solution
boolean isValidUsername(String username) {
    return username.length() >= 10;
}

// Overprocessed version
class ValidationContext {
    private final Map<String, Integer> rules;

    ValidationContext(Map<String, Integer> rules) {
        this.rules = rules;
    }

    boolean validate(String key, String value) {
        return value.length() >= rules.getOrDefault(key, 0);
    }
}
