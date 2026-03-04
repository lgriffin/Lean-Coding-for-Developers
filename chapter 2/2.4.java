@Test
void createsUser_integration() {
    UserService service = new UserService(
        new RealDatabase(),
        new RealEmailClient()
    );

    service.createUser("user@example.com");
