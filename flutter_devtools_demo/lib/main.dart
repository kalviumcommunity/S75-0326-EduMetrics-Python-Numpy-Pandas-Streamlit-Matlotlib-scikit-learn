import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    debugPrint('🚀 MyApp initialized');

    return MaterialApp(
      title: 'Flutter Demo - DevTools Showcase',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter DevTools Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int count = 0;
  final List<String> logHistory = [];

  @override
  void initState() {
    super.initState();
    debugPrint('✅ MyHomePage initialized - State created');
  }

  /// 🔥 HOT RELOAD DEMO:
  /// Try editing the text below and saving (Ctrl+S)
  /// The UI will update instantly without restarting the app!
  /// Notice how the counter value is preserved.
  void increment() {
    setState(() {
      count++;
      final logMessage = 'Count updated to $count';
      logHistory.add(logMessage);

      debugPrint('📊 [DEBUG] $logMessage');
      debugPrint('📋 [STATS] Total increments: $count');
      debugPrint('⏱️  [TIME] Updated at ${DateTime.now()}');
    });
  }

  void decrement() {
    setState(() {
      count--;
      final logMessage = 'Count reduced to $count';
      logHistory.add(logMessage);

      debugPrint('📊 [DEBUG] $logMessage');
      debugPrint('⬇️  [ACTION] Decrement button pressed');
    });
  }

  void reset() {
    setState(() {
      count = 0;
      logHistory.clear();

      debugPrint('🔄 [RESET] Counter reset to 0');
      debugPrint('🧹 [CLEANUP] Log history cleared');
    });
  }

  void showDevToolsInfo() {
    debugPrint('ℹ️  [INFO] Opening DevTools information...');

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('🛠️ How to Use Flutter DevTools'),
          content: const SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                SectionTitle(title: '1. Open DevTools'),
                Text(
                  '• In VS Code: Run "Flutter: Open DevTools" from Command Palette\n'
                  '• Or run: flutter pub global run devtools',
                  style: TextStyle(fontSize: 12),
                ),
                SizedBox(height: 12),
                SectionTitle(title: '2. Widget Inspector'),
                Text(
                  '• Click the widget icon in DevTools\n'
                  '• Click on any UI element in your app\n'
                  '• See the widget tree and corresponding code',
                  style: TextStyle(fontSize: 12),
                ),
                SizedBox(height: 12),
                SectionTitle(title: '3. Performance Tab'),
                Text(
                  '• Monitor FPS (frames per second)\n'
                  '• Check for dropped frames or jank\n'
                  '• Identify performance bottlenecks',
                  style: TextStyle(fontSize: 12),
                ),
                SizedBox(height: 12),
                SectionTitle(title: '4. Memory Tab'),
                Text(
                  '• Track memory usage over time\n'
                  '• Detect memory leaks\n'
                  '• Monitor garbage collection',
                  style: TextStyle(fontSize: 12),
                ),
                SizedBox(height: 12),
                SectionTitle(title: '5. Debug Console'),
                Text(
                  '• Check this app\'s debugPrint() outputs here\n'
                  '• All logs appear with timestamps\n'
                  '• Useful for tracking variable values',
                  style: TextStyle(fontSize: 12),
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Got it!'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // 🔥 HOT RELOAD SECTION
              Card(
                color: Colors.amber.shade50,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        '🔥 Hot Reload Feature',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: Colors.amber,
                        ),
                      ),
                      const SizedBox(height: 12),
                      const Text(
                        '💡 Tip: Edit ANY text in this app and press Ctrl+S. '
                        'The UI updates instantly without losing app state!',
                        style: TextStyle(fontSize: 12, color: Colors.brown),
                      ),
                      const SizedBox(height: 12),
                      TextField(
                        readOnly: true,
                        decoration: InputDecoration(
                          hintText: 'Try editing the hint text!',
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 24),

              // 📊 COUNTER SECTION
              Card(
                color: Colors.blue.shade50,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      const Text(
                        '📊 Counter Value',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 20),
                      Text(
                        '$count',
                        style: const TextStyle(
                          fontSize: 72,
                          fontWeight: FontWeight.bold,
                          color: Colors.blue,
                        ),
                      ),
                      const SizedBox(height: 20),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          ElevatedButton.icon(
                            onPressed: decrement,
                            icon: const Icon(Icons.remove),
                            label: const Text('Decrease'),
                          ),
                          ElevatedButton.icon(
                            onPressed: increment,
                            icon: const Icon(Icons.add),
                            label: const Text('Increase'),
                          ),
                        ],
                      ),
                      const SizedBox(height: 12),
                      ElevatedButton.icon(
                        onPressed: reset,
                        icon: const Icon(Icons.refresh),
                        label: const Text('Reset'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.red,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 24),

              // 📋 DEBUG CONSOLE SECTION
              Card(
                color: Colors.green.shade50,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        '📋 Debug Console Output',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.green,
                        ),
                      ),
                      const SizedBox(height: 12),
                      const Text(
                        '👀 Check your VS Code Debug Console to see these outputs:',
                        style: TextStyle(fontSize: 12, color: Colors.green),
                      ),
                      const SizedBox(height: 12),
                      Container(
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: Colors.black87,
                          borderRadius: BorderRadius.circular(8),
                          fontFamily: 'monospace',
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: logHistory.isEmpty
                              ? const [
                                  Text(
                                    '> Waiting for logs...',
                                    style: TextStyle(
                                      color: Colors.grey,
                                      fontFamily: 'Courier New',
                                    ),
                                  )
                                ]
                              : logHistory
                                  .asMap()
                                  .entries
                                  .map(
                                    (entry) => Text(
                                      '[${entry.key + 1}] ${entry.value}',
                                      style: const TextStyle(
                                        color: Colors.greenAccent,
                                        fontFamily: 'Courier New',
                                        fontSize: 11,
                                      ),
                                    ),
                                  )
                                  .toList(),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 24),

              // 🛠️ DEVTOOLS SECTION
              Card(
                color: Colors.purple.shade50,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        '🛠️ Flutter DevTools Guide',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.purple,
                        ),
                      ),
                      const SizedBox(height: 12),
                      const Text(
                        'Use DevTools to inspect widgets, monitor performance, '
                        'track memory, and debug your Flutter app in real-time.',
                        style: TextStyle(fontSize: 12),
                      ),
                      const SizedBox(height: 16),
                      SizedBox(
                        width: double.infinity,
                        child: ElevatedButton.icon(
                          onPressed: showDevToolsInfo,
                          icon: const Icon(Icons.info),
                          label: const Text('Show DevTools Instructions'),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Colors.purple,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 24),

              // 📖 HOW IT WORKS
              Card(
                color: Colors.orange.shade50,
                child: const Padding(
                  padding: EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        '📖 Demonstration Workflow',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.orange,
                        ),
                      ),
                      SizedBox(height: 12),
                      Text(
                        '1. Click "Increase" or "Decrease" buttons\n'
                        '2. Check VS Code\'s Debug Console for debugPrint() outputs\n'
                        '3. Edit UI text and save (Ctrl+S) to see Hot Reload in action\n'
                        '4. Open DevTools to:\n'
                        '   • Use Widget Inspector to click UI elements\n'
                        '   • Check Performance tab for FPS\n'
                        '   • Monitor Memory usage\n'
                        '5. Notice app state is preserved after Hot Reload!',
                        style: TextStyle(fontSize: 12, height: 1.6),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 32),
            ],
          ),
        ),
      ),
    );
  }
}

class SectionTitle extends StatelessWidget {
  final String title;

  const SectionTitle({Key? key, required this.title}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text(
      title,
      style: const TextStyle(
        fontWeight: FontWeight.bold,
        fontSize: 13,
        color: Colors.deepPurple,
      ),
    );
  }
}
