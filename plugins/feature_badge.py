from __future__ import annotations


class FeatureBadgePlugin:
    def on_page(self, page, site):
        featured = bool(page.metadata.get("featured"))
        badge = page.metadata.get("badge") or ("Featured" if featured else "")
        page.extra["feature_badge"] = badge
        page.extra["feature_class"] = "page--featured" if featured else ""
        page.extra["tag_list"] = ", ".join(str(tag) for tag in page.metadata.get("tags", []))
        return page


def register():
    return FeatureBadgePlugin()
