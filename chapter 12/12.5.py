def check_migration_rollback(migration_file: str) -> bool:
    """Reject migrations that lack a reverse operation."""
    content = read_file(migration_file)
    has_forward = "def upgrade(" in content or "def forwards(" in content
    has_reverse = "def downgrade(" in content or "def backwards(" in content

    if has_forward and not has_reverse:
        raise MigrationError(
            f"{migration_file} has no rollback. Add a downgrade() function "
            f"or set IRREVERSIBLE=True with tech lead approval."
        )
    return True
