Exception in thread "main" java.lang.NullPointerException
    at UserService.applyPreferences(UserService.java:47)
    at UserController.getProfile(UserController.java:23)
    at …
// Symptom fix: guard against null
public void applyPreferences(User user, Preferences prefs) {
    if (prefs != null) {
        user.setTheme(prefs.getTheme());
    }
}
