class quin {
  static void Main() {
    var s = @"class quin {{
      static void Main() {{
        var s = {0}{1}{0};
        System.Console.WriteLine(s, (char)34, s);
      }}
    }}";
    System.Console.WriteLine(s, (char)34, s);
  }
}
