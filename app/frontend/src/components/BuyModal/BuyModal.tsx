import { useState } from "react";

import { Modal, IconButton, DefaultButton, TextField } from "@fluentui/react";

import styles from "./BuyModal.module.css";

interface Props {
    isBuy: boolean;
    setIsBuy: (isBuy: boolean) => void;
    address: string;
    setAddress: (address: string) => void;
}

export const BuyModal = ({ setIsBuy, setAddress, isBuy, address }: Props) => {
    const onAddressChange = (_ev: React.FormEvent<HTMLInputElement | HTMLTextAreaElement>, newValue?: string) => {
        if (!newValue) {
            setAddress("");
        } else {
            setAddress(newValue);
        }
    };

    return (
        <Modal className={styles.buyContainer} isOpen={isBuy} onDismiss={() => setIsBuy(false)} isBlocking={true}>
            <div>
                <IconButton iconProps={{ iconName: "Cancel" }} ariaLabel="Close popup modal" onClick={() => setIsBuy(false)} />
                <div className={styles.buyContainer}>
                    <div className={styles.buyMessage}>Enter your address:</div>
                </div>
                <div className={styles.buyContainer}>
                    <TextField className={styles.buyInput} value={address} onChange={onAddressChange} multiline resizable={false} borderless />
                </div>
                <div className={styles.buyContainer}>
                    <DefaultButton className={styles.buyMessage} onClick={() => setIsBuy(false)}>
                        Buy Now?
                    </DefaultButton>
                </div>
            </div>
        </Modal>
    );
};
