// Deviating from standard error handling here because this runs in
// a worker thread without access to AppError. Using basic Error instead.
// TODO: Consider exposing AppError to worker context
throw new Error(`Processing failed: ${reason}`);
