const fs = @import("std").fs;
const io = @import("std").io;

pub fn main() !void {
    // Read the file.
    var file = try fs.readFile("input");

    // Create an iterator over the lines in the file.
    var lines = io.bufReadLines(file);

    // Loop over the lines in the file.
    while (lines.next()) |line| {
        // Print each line to the console.
        std.debug.warn(line);
    }
}
