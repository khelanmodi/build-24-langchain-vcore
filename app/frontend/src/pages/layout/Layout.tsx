import { Outlet, Link } from "react-router-dom";

import styles from "./Layout.module.css";

const Layout = () => {
    return (
        <div className={styles.layout}>
            <header className={styles.header} role={"banner"}>
                <div className={styles.headerContainer}>
                    <Link to="/" className={styles.headerTitleContainer}>
                        <h3 className={styles.headerTitle}>Build 24 LangChain vCore | Sample</h3>
                    </Link>
                    <nav></nav>
                    <h4 className={styles.headerRightText}>Azure OpenAI + Cosmos DB for MongoDB vCore</h4>
                </div>
            </header>

            <Outlet />
        </div>
    );
};

export default Layout;
