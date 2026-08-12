// Root cause fix: guarantee preferences exist
public User registerUser(String email, String password) {
    User user = new User(email, password);
    Preferences defaults = new Preferences("light", "en", true);
    userRepository.save(user);
    preferencesRepository.save(user.getId(), defaults);
    return user;
}
