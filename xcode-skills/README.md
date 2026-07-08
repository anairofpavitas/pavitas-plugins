# xcode-skills

Apple's official Xcode and Swift engineering skills, bundled so they install and update as one
plugin instead of seven separate uploads. Loads as `xcode-skills:<name>`.

## Skills

| Skill | What it does |
|---|---|
| `xcode-skills:swiftui-specialist` | Authoritative SwiftUI best-practice and performance guidance from Apple — view structure, data flow (`@State`/`@Binding`/`@Observable`), environment, `ForEach`/`List` identity, localization, animations, and soft-deprecated APIs. Consult for any SwiftUI review or code generation. |
| `xcode-skills:swiftui-whats-new-27` | New SwiftUI APIs, behaviors, and deprecations in the 2027 OS releases (SDK 27: iOS/macOS/watchOS/tvOS/visionOS 27) — the `@State` macro migration, `@ContentBuilder`, `reorderable()`, `AsyncImage(request:)`, swipe actions outside `List`, toolbar overflow, `sheet(item:)`, and document-based apps. |
| `xcode-skills:uikit-app-modernization` | Modernizes UIKit apps for multi-window environments — replaces legacy shared-state APIs (`mainScreen`, `interfaceOrientation`, app/scene lifecycle, safe-area inset updates) with context-appropriate alternatives. |
| `xcode-skills:modernize-tests` | Migrates XCTest suites to Swift Testing and restructures existing Swift Testing code to adopt newer features. |
| `xcode-skills:c-bounds-safety` | Guide to the C `-fbounds-safety` language extension — the language model, pointer annotations (`__counted_by`, `__sized_by`, `__ended_by`, etc.), adoption in existing C, build settings, and runtime debugging of bounds violations. |
| `xcode-skills:audit-xcode-security-settings` | Audits an Xcode project's security posture and progressively enables hardening — compiler warnings, static-analyzer checkers, and Enhanced Security build settings and entitlements for C/C++/Objective-C/Swift. |
| `xcode-skills:device-interaction` | Verifies iOS app behavior on device or simulator via screenshots, UI hierarchy inspection, and touch interactions. |

## Source and authorship

These skills were written and published by Apple as authoritative Xcode/Swift engineering
guidance; several explicitly supersede prior model training on their topics. They are bundled
here unmodified for the `pavitas-plugins` marketplace — only packaged into plugin form (manifest
+ this README). Each skill keeps its own `references/` (and `audit-xcode-security-settings` its
`scripts/`) intact.

## Connectors

None bundled. The skills use whatever file tools and Xcode/simulator/device tooling the session
already has. No `.mcp.json`.
