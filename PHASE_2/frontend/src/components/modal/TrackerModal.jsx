import React from 'react';
import Modal, { ModalBody, ModalHeader } from './Modal';

const TrackerModal = (props) => {
    return (
        <Modal
            show={props.trackerOpen}
            setShow={props.setTrackerOpen}
            className="trackerModal"
            >
            <ModalHeader >
                <h2>COVID-19 Tracker</h2>
            </ModalHeader>
            <ModalBody >
            <iframe src="https://bing.com/covid" title="bing-covid-19-tracker" style={{width: "100%", height:"400px"}}></iframe>
            </ModalBody>
        </Modal>
    );
}

export default TrackerModal;