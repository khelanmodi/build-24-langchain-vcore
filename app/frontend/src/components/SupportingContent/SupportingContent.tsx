import { parseSupportingContentItem } from "./SupportingContentParser";

import styles from "./SupportingContent.module.css";

interface Props {
    supportingContent: string[] | { json: string[] };
}

export const SupportingContent = ({ supportingContent }: Props) => {
    const textItems = Array.isArray(supportingContent) ? supportingContent : supportingContent.json;
    return (
        <ul className={styles.supportingContentNavList}>
            {textItems.map((c, ind) => {
                const parsed = parseSupportingContentItem(c);
                return (
                    <li className={styles.supportingContentItem} key={ind}>
                        <h4 className={styles.supportingContentItemHeader}>{parsed.title}</h4>
                        <p className={styles.supportingContentItemText} dangerouslySetInnerHTML={{ __html: parsed.content }} />
                    </li>
                );
            })}
        </ul>
    );
};
